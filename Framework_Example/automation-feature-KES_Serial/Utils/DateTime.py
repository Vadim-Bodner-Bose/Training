import time


class DateTime:

    @staticmethod
    def get_current_datetime():
        return time.strftime("%Y_%m_%d_%H-%M-%S")

    @staticmethod
    def explicit_wait(secs=2):
        time.sleep(secs)
