class Log(object):
    message = ""
    level = ""

    def __init__(self, header, **entries):
        self.header = header
        self.__dict__.update(entries)