# Singleton Pattern generates only one object/instance of the class - can be used in properties/data base connections etc...
class Logger(object):
    # private variable instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)

        else:
            raise ValueError("Instance can only be generated once per Singleton Pattern")
            # Put any initialization here.

        return cls._instance
    # store data in singleton
    def SetData(self, num):
        self.data = num
    # retrieve data from singleton
    def GetData(self):
        print(self.data)


log1 = Logger()
log1.SetData(5)
log1.GetData()
log2 = Logger()
