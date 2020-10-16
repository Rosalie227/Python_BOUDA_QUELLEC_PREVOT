from math import *
from enum import Enum


class Unit:

    def __init__(self, id: int, name : str):
        self.attribut1 = id
        self.attribut2 = name

    def Unit (id : int, name : str) :


class IndicatorGroup (Enum):

    def __init__(self):
        super().__init__()

    EXPORTS_AND_IMPORTS = 1.1
    SUPPLY_AND_USE = 1.2
    PRICES = 1.3
    FEED_PRICE_RATIOS = 1.4
    QUANTITIES_FED = 1.5
    TRANSPORTATION = 1.6
    ANIMAL_UNIT_INDEXES = 1.7
        
        
class CommodityGroup (Enum) :
    
    def __init__(self):
        super().__init__()

    CORN = 2.1
    BARLEY = 2.2
    OATS = 2.3
    SORGHUM = 2.4
    BYPRODUCTS_FEEDS = 2.5
    COARS_GRAINS = 2.6
    HAY = 2.7
    FEED_GRAINS = 2.8
    ANIMAL_PROTEINS_FEEDS = 2.9
    PROCESSED_FEEDS = 2.01
    ENERGY_FEEDS = 2.02
    OTHER = 2.03
      
    
class Commodity :
    def __init__(self):
        super().__init__()
    id : str
    name : str

    def Commodity (group : CommodityGroup, id : str, name : str) :


        

class Indicator (Unit, IndicatorGroup):
    def __init__(self, id: str, frequency: int, frequencyDesc: str, geogLocation: str, name: str):
        super().__init__(id)
        self.attribut2 = frequency
        self.attribut3 = frequencyDesc
        self.attribut4 = geogLocation

    def Indicator (id : str, frequency : int, frequencyDesc : str, geogLocation : str, unit : Unit, indicatorGroup : IndicatorGroup) :



class Measurement:

    def __init__(self, year: int, value: float, timeperiodeId: int, timeperiodDescr: str):
        self.attribut1 = year
        self.attribut2 = value
        self.attribut3 = timeperiodeId
        self.attribut4 = timeperiodDescr

    def Measurement(id: int, year: int, value: float, timeperiodeId: int, timeperiodDescr: str, commodity: Commodity, indicator: Indicator):
