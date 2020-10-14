from math import *


class Unit:

    def __init__(self, id: int, name : str):
        self.attribut1 = id
        self.attribut2 = name

    def Unit (id : int, name : str) :


class IndicatorGroup (Enum):

    def __init__(self):
        super().__init__()

class CommodityGroup :


class Commodity :
    def __init__(self):
        super().__init__()
    id : str
    name : str

    def Commodity (group : CommodityGroup, id : str, name : str) :

#---#

class Indicator (Unit, IndicatorGroup):
    def __init__(self, id: str, frequency: int, frequencyDesc: str, geogLocation: str, name: str):
        super().__init__(id)
        self.attribut2 = frequency
        self.attribut3 = frequencyDesc
        self.attribut4 = geogLocation

    def Indicator (id : str, frequency : int, frequencyDesc : str, geogLocation : str, unit : Unit, indicatorGroup : IndicatorGroup) :

#---#

class Measurement:

    def __init__(self, year: int, value: float, timeperiodeId: int, timeperiodDescr: str):
        self.attribut1 = year
        self.attribut2 = value
        self.attribut3 = timeperiodeId
        self.attribut4 = timeperiodDescr

    def Measurement(id: int, year: int, value: float, timeperiodeId: int, timeperiodDescr: str, commodity: Commodity, indicator: Indicator):


