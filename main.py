from math import *
from enum import Enum
from abc import abstractmethod, abstractclassmethod
from enum import Enum

@abstractclassmethod
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

    def __init__(self):
        super().__init__()

    def volume(self,id: int, name: str = 'Volume'):
        print(self.name + id)

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
        
        
