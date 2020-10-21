from math import *
from enum import Enum
from abc import abstractmethod, abstractclassmethod

@abstractclassmethod
class Unit:

    def __init__(self, id: int, name : str):
        self.attribut1 = id
        self.attribut2 = name



class IndicatorGroup (Enum):

    EXPORTS_AND_IMPORTS = 1
    SUPPLY_AND_USE = 2
    PRICES = 3
    FEDD_PRICE_RATIONS = 4
    QUANTITIES_FED = 5
    TRANSPORTATION = 6
    ANIMAL_UNIT_INDEXES = 7

        
        
class CommodityGroup (Enum) :

    CORN = 1
    BARLEY = 2
    OATS = 3
    SORGHUM = 4
    BYPRODUCTS_FEEDS = 5
    COARSE_GRAINS = 6
    HAY = 7
    FEED_GRAINS = 8
    ANIMAL_PROTEIN_FEEDS = 9
    GRAIN_PROTEIN_FEEDS = 10
    PROCESSED_FEEDS = 11
    ENERGY_FEEDS = 12
    OTHER = 13

    
    
class Commodity :
    
    def __init__(self):
        super().__init__()
    id : str
    name : str

        

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
 


#Volume
class Volume :

    def __init__(self, id: int, name: str = 'Volume'):
        super().__init__()
        self.attribut1 = id
        self.attribut2 = name
        

#Surface
class Surface :

    def __init__(self, name: str):
        self.attribut1 = name

    def surface(self,id: int, name: str = "Surface"):
        print(self.name + id)

#Price
class Price :

    def __init__(self):
        super().__init__()

    def price(self,id: int, name: str = 'Price'):
        print(self.name + id)

#Count
class Count :

    def __init__(self, what: str):
        self.attribut1 = what

    def count(self,id: int, name: str = "Count", what: str):
        print(self.name + id)

#Weight
class Weight :

    def __init__(self, multiplier: float):
        self.attribut1 = multiplier

    def weight(self,id: int, name: str = "Weight", multiplier: float):
        print(self.name + id)

#Ratio
class Ratio :

    def __init__(self):
        super().__init__()
     
    
     
class Describable :

    @abstractmethod
    def describe (self) :

    def ratio(self,id: int, name: str = 'Ratio'):
        print(self.name + id)
        
# FoodCropFactory
class FoodCropFactory :
    def __init__(self):
        super().__init__()

    def createVolume(self,id : int) -> Unit :

    def createPrice(self,id : int) -> Unit :

    def createWeight(self,id:int,weight:float) -> Unit :

    def createSurface(self,id:int) -> Unit :

    def createCount(self,id:int,what:str) -> Unit:

    def createRatio(self,id:int) -> Unit:

    def createUnitRatio(self,id:int,unit1:Unit,unit2:Unit) -> Unit:

    def createCommodity(self,group:CommodityGroup,id:int,name:str) -> Commodity:

    def createIndicator(self,id:int,frequency:int,freqDesc:str,geogLocation:str,indicatorGroup:IndicatorGroup,unit:Unit) -> Indicator:

    def createMeasurementType(self,id:int,description:str) -> MeasurementType:

    def createMeasurement(id:int,year:int,value:float,timeperiodId:int,timeperiodDesc:str,commodity:Commodity,indicator:Indicator) -> Measurement:

#FoodCropsDataset
class FoodCropsDataset:

    def __init__(self):
        super().__init__()

    def load(self,datasetPath:str):

    def findMeasurements(self,commodityType:CommodityType=nil,indicatorGroup:IndicatorGroup=nil,geographicalLocation:str=nil,unit:Unit=nil) -> List[Measurement]:
