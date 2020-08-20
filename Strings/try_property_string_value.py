class Parser():
    """Class Parser is the factory for all the parsers we are going to employ"""

    # @classmethod
    # def arenal_parser(cls):
    #     return ArenalParser()
    #
    # @classmethod
    # def connectivity_parser(cls):
    #     return ConnectivityParser()
    response = ""
    is_ar_idle = 'is_ar_idle'
    is_ar_standby = 'is_ar_standby'
    is_wifi_prof_eq_one = 'is_wifi_prof_eq_one'
    is_wifi_prof_eq_zero = 'is_wifi_prof_eq_zero'

    @classmethod
    def continous_read(cls):
        cls.response = True
        # print(cls.response)

    @classmethod
    def get_parser(cls, parse_format):
        """A static method to get a table"""
        try:
            if parse_format == cls.is_ar_standby:
                print("is in standby")
            if parse_format == cls.is_ar_idle:
                cls.continous_read()
                return cls.response
            if parse_format == cls.is_wifi_prof_eq_one:
                print("is one")
            if parse_format == cls.is_wifi_prof_eq_zero:
                print("is zero")
        except AssertionError:
            print("Parser Type isn't implemented")
            return None


# print(Parser.is_ar_idle)
Parser.continous_read.get_parser(Parser.is_ar_idle)
# if Parser.get_parser(Parser.is_ar_idle):
#     print('pass')
