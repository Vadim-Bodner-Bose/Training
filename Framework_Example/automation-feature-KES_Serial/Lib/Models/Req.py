class Req(object):
    id = None
    cmd = ""
    recipe = {}

    def __init__(self, header, **entries):
        self.header = header
        self.__dict__.update(entries)

    def isRecipeEqual(self, recipe):
        return self.recipe == recipe

    def isCmdEqual(self, cmd):
        return self.cmd == cmd

    def isSourceEqual(self, source):
        return self.header.source == source