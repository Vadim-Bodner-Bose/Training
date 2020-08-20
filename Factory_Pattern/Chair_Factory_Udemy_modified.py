from abc import ABCMeta, abstractstaticmethod

# the interface fullfilss the exact descritpion of a pattern by the gang of four, however the pattern will work w/o it also.
class IChair(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """The Chair Interface"""

    @abstractstaticmethod
    def dimensions():
        """A static inteface method"""


class BigChair(IChair):  # pylint: disable=too-few-public-methods
    """The Big Chair Concrete Class which implements the IChair interface"""

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}


class MediumChair(IChair):  # pylint: disable=too-few-public-methods
    """The Medium Chair Concrete Class which implements the IChair interface"""

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}


class SmallChair(IChair):  # pylint: disable=too-few-public-methods
    """The Small Chair Concrete Class which implements the IChair interface"""

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height}


class ChairFactory:  # pylint: disable=too-few-public-methods
    """Tha Factory Class"""

    @classmethod
    def get_chair(cls,chair):
    # @staticmethod
    # def get_chair(chair): static method also works, but class methods are suggested for Factory implementation in letaruture
    # class method also allows to inherit from this class and call the factory from a child class.
        """A static or class method to get a table"""
        try:
            if chair == "BigChair":
                return BigChair()
            if chair == "MediumChair":
                return MediumChair()
            if chair == "SmallChair":
                return SmallChair()
            raise AssertionError("Chair Not Found")
        except AssertionError as _e:
            print(_e)
        return None
    @staticmethod
    def small_chair():
        return SmallChair()

if __name__ == "__main__":
    # either call of Chari Factory below works
    # CHAIR_FACTORY = ChairFactory().get_chair("SmallChair")
    # CHAIR_FACTORY = ChairFactory.get_chair("SmallChair")
    # print(CHAIR_FACTORY.dimensions())
    print(ChairFactory.get_chair("SmallChair").dimensions())
    print(ChairFactory.small_chair().dimensions())