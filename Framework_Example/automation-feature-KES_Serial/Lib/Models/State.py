import logging


class State(object):
    brewing_status = ""
    recipe = {}
    mode = {}
    info = ""
    dispensed = None

    def __init__(self, header, **entries):
        self.header = header
        self.__dict__.update(entries)

    def isRecipeEqual(self, recipe):
        return self.recipe == recipe

    def isModeEqual(self, mode, req_id):
        mode["req_id"] = req_id
        self.mode.pop('brew_lock_causes', None)
        logging.warning("mode is: {}".format(self.mode))
        return self.mode == mode

    def isBrewingStatusEqual(self, brewing_status):
        return self.brewing_status == brewing_status
