"""
Handles all things serial. Super serial

"""

import serial
import time


class SerialConnection:
    """
    Base class that establishes connection to COM ports, sends data, and receives data to the brewers

    """

    def __init__(self, **kwargs):
        """
        Class initialization

        """
        self.board_connection = None
        self.board_type = None
        self.com_port = None
        self.baud_rate = None
        self.write_timeout = None
        self.response_list = []
        # generate required parameters from **kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def establish_connection(self):
        """
        Establishes connection to board via COM port.
        """
        try:
            self.board_connection = serial.Serial(port=self.com_port, baudrate=self.baud_rate,
                                                  timeout=self.write_timeout,
                                                  parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                                  write_timeout=self.write_timeout)
        except IOError as e:
            raise AssertionError("One of the required parameters is missing")
        if self.board_connection.isOpen() is not True:
            raise AssertionError

    def close_connection(self):
        """
        Closes the COM port connection
        """
        self.board_connection.close()

    def serial_login(self):
        """
        This supports the check for logging into sandstone and FVT mode for arenal
        """
        try:
            self.board_connection.write(b'\r\n')
            response = self.board_connection.readline().decode('utf-8')
            if 'login' or 'Password' in response:
                self.board_connection.write(b'root\r\n')
            elif "$" or 'tty' in response:
                pass
            else:
                time.sleep(160)
                self.board_connection.write(b'root\r\n')
        except IOError as e:
            self.board_connection.write(b'root\r\n')

    def send_receive_data(self, send_data, receive_data, lines_to_read=6):
        """
        Sends data to board via serial connection and check for expected response

        """
        self.send_data(send_data)
        return self.read_data(receive_data, lines_to_read)

    def send_data(self, send_data):
        """
                Sends data to board via serial connection

        """
        self.board_connection.flushInput()
        self.board_connection.flushOutput()
        self.board_connection.write(str(send_data + '\r\n').encode('utf-8'))
        print("SENDING DATA: {}".format(send_data))

    def read_data(self, receive_data, lines_to_read=6):
        """
                Read data from the serial port
        """
        data_counter = 0
        while True:
            response = self.board_connection.readline().decode('utf-8')
            print("response is: {}".format(response.strip("> ")))
            if response is None or '$' in response or "Unsupported" in response:
                continue

            val = response.strip("\r\n")
            if val.isdigit():
                if int(val) in receive_data:
                    return int(val)
                else:
                    return False
            elif receive_data in response:
                return True

            else:
                print("SERIAL RESPONSE ATTEMPT: {}".format(data_counter))
                if data_counter < lines_to_read:
                    data_counter += 1
                else:
                    return False

    def continuous_send_receive_data(self, send_data, receive_data, lines_to_read):
        """
        Sends data to board via serial connection continuously, stores the data in a list and returns the list for \
        post-processing

        """
        self.board_connection.flushInput()
        self.board_connection.flushOutput()
        # allow for cases when you just want to read the response
        if send_data is not None:
            self.board_connection.write(str(send_data + '\r\n').encode('utf-8'))
        self.response_list = []
        lines_to_read = lines_to_read
        lines_read = 0
        while True:
            response = self.board_connection.readline().decode('utf-8')
            self.response_list.append(response)  # builds a list of all responses to be post-processed
            lines_read += 1
            if send_data in response:
                continue
            elif receive_data in response:
                return self.response_list
            elif lines_to_read <= lines_read:
                # if number of lines read is great than expected - exit and return the list of responses
                return self.response_list

