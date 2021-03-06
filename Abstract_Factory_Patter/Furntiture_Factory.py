from abc import ABCMeta, abstractstaticmethod
from Chair_Factory import ChairFactory
from Table_Factory import TableFactory


class IFurnitureFactory(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """Furniture Factory Interface"""

    @abstractstaticmethod
    def get_furniture(furniture):
        """The static funiture factory inteface method"""


class FurnitureFactory(IFurnitureFactory):  # pylint: disable=too-few-public-methods
    """The Furniture Factory Concrete Class"""

    @staticmethod
    def get_furniture(furniture):
        """Static get_furniture method"""
        try:
            if furniture in ["SmallChair", "MediumChair", "BigChair"]:
                return ChairFactory().get_chair(furniture)
            if furniture in ["SmallTable", "MediumTable", "BigTable"]:
                return TableFactory().get_table(furniture)
            raise AssertionError("No Furniture Factory Found")
        except AssertionError as _e:
            print(_e)
        return None


FURNITURE = FurnitureFactory.get_furniture("SmallChair")
print(f"{FURNITURE.__class__} : {FURNITURE.dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("MediumTable")
print(f"{FURNITURE.__class__} : {FURNITURE.dimensions()}")
