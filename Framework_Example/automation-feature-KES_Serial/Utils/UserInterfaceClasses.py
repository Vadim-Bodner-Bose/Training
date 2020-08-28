# various useful methods grouped by class

class VerboseMessages():
    def __init__(self):
        pass

    #yes or no ui
    def yes_or_no(self,question):
        while "the answer is invalid":
            reply = str(input(question + ' (y/n): ')).lower().strip()
            if reply[0] == 'y':
                return True
            if reply[0] == 'n':
                return False


#  Testing
# vb = VerboseMessages.yes_or_no("", "Did you reboot?")
#
# print(vb == True)