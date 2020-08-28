class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class LocatorError(Error):
    """Exception raised for missing Locators.

    Attributes:
        locators -- input locators for which the error occurred
        message -- explanation of the error
    """

    def __init__(self, locators, message):
        self.locators = locators
        self.message = message
