from math import *
from enum import Enum
from abc import ABC, abstractmethod, abstractclassmethod
import pandas


class Describable(ABC):  # ABC = Abstract Base Class

    # constructor
    def __init__(self):
        super().__init__()

    @abstractmethod
    def describe(self) -> str:
        pass  # on note pass car il s'agit d'une méthode abstraite


@abstractclassmethod
class Unit(ABC, Describable):  # j'ai rajouté ABC pour dire que c'est une classe abstraite
    id: int
    name: str

    def __init__(self, id: int, name: str):
        super().__init__()
        self.id = id
        self.name = name

    def describe(self):
        pass  # compléter cette méthode describe / est ce que les sous-classes de unit hérite de describe?
    #print("i=",i)


class Volume(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Volume')

    def describe(self) -> str:  # ils veulent absolument que ce soit une property
        return "hi"


class Surface(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Surface')


class Price(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Price')


class Count(Unit):
    __what: str  # le underscore signifie que l'attribue est privé

    def __init__(self, id: int, what: str):
        super().__init__(id, name='Count')
        self.__what = what  # attribut _what prend valeur what


class Weight(Unit):
    __multiplier: float  # attribut privé

    def __init__(self, id: int, multiplier: float):
        super().__init__(id, name='Weight')
        self.__multiplier = multiplier  # attribut _multiplier prend valeur multiplier


class Ratio(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Ratio')


class Date(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Date')


class Indicator(Describable):
    idIndicator: int    # attribut public
    __frequency: int
    __frequencyDesc: str
    __geogLocation:str
    __indicatorGroup: IndicatorGroup
    __unit: Unit

    def __init__(self, idIndicator: int, frequency: int, frequencyDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                 unit: Unit):
        super().__init__()
        self.idIndicator = idIndicator
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation
        self.__indicatorGroup = indicatorGroup
        self.__unit = unit

    def describe(self):
        pass    # compléter cette méthode


class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 1 # garder ces numéros ou les changer en fonction de la database
    SUPPLY_AND_USE = 2
    PRICES = 3
    FEDD_PRICE_RATIONS = 4
    QUANTITIES_FED = 5
    TRANSPORTATION = 6
    ANIMAL_UNIT_INDEXES = 7


class Commodity(Describable):
    id: int
    __name: str
    __group: CommodityGroup

    def __init__(self, id: int, name: str, group: CommodityGroup):
        super().__init__()
        self.id = id
        self.__name = name
        self.__group = group

    def describe(self):
        pass    # à compléter


class CommodityGroup(Enum): # idem, garder les mêmes chiffres ou non
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


class Measurement(Describable):
    __id: int
    __year: int
    __value: float
    __timePeriodId: int
    __timePeriodDescr: str
    __commodity: Commodity
    __indicator: Indicator

    def __init__(self, id: int, year: int, value: float, timeperiodeId: int, timeperiodDescr: str, commodity: Commodity,
                 indicator: Indicator):
        super().__init__()
        self.__id = id
        self.__year = year
        self.__value = value
        self.__timePeriodId = timeperiodeId
        self.__timePeriodDescr = timeperiodDescr
        self.__commodity = commodity
        self.__indicator = indicator

    def describe(self):
        pass    # à compléter


# FoodCropFactory
class FoodCropFactory:

    def __init__(self):
        super().__init__()
        self.units_registry = {}  # à modifier peut-être peut-être pas des {} / à initialiser comment?
        self.commodity_registry = {}
        self.indicator_registry = {}

    def createVolume(self, id: int) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]
        else:
            instance = Volume(id)
            self.units_registry[id] = instance
            return instance

    def createPrice(self, id: int) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]  # L'instance existe déjà pour la clé id dans le dictionnaire, on la renvoie
        else:
            instance = Price(id)  # L'instance n'existe pas encore pour id, on la créé
            self.units_registry[id] = instance  # On l'associe à la clé id dans le dictionnaire (ajout)
            return instance  # On la renvoie

    def createWeight(self, id: int, multiplier: float) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]
        else:
            instance = Weight(id, multiplier)
            self.units_registry[id] = instance
            return instance

    def createSurface(self, id: int) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]
        else:
            instance = Surface(id)
            self.units_registry[id] = instance
            return instance

    def createCount(self, id: int, what: str) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]
        else:
            instance = Count(id, what)
            self.units_registry[id] = instance
            return instance

    def createRatio(self, id: int) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]
        else:
            instance = Ratio(id)
            self.units_registry[id] = instance
            return instance

    # rajouter un createDate
    def createDate(self, id: int) -> Unit:
        if id in self.units_registry:
            return self.units_registry[id]
        else:
            instance = Date(id)
            self.units_registry[id] = instance
            return instance

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Commodity:
        if id in self.commodity_registry:
            return self.commodity_registry[id]
        else:
            instance = Commodity(id, name, group)
            self.commodity_registry[id] = instance
            return instance

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: int,   # erreur de type pour Enum
                        unit: Unit) -> Indicator:
        if id in self.indicator_registry:
            return self.indicator_registry[id]
        else:
            instance = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)   #erreur de type
            self.indicator_registry[id] = instance
            return instance

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          commodity: Commodity, indicator: Indicator) -> Measurement:
        instance = Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
        return (instance)
        # à vérifer


# FoodCropsDataset
class FoodCropsDataset:

    # constructeur
    def __init__(self):  # revérifier la relation
        super().__init__()
        self.dicoCommodityGroup = {}  # les 4 dicos en attributs / notations???
        self.dicoIndicatorGroup = {}
        self.dicoLocGeo = {}
        self.dicoUnit = {}

    def load(self, datasetPath: str):
        datasetPath = 'C:\\Users\\charl\\Documents\\2A EMA\\poo\\Projet Python\\FeedGrains.csv'
        dataframe = pandas.read_csv(datasetPath)  # charge le fichier

        # instanciations du modèle
        for index, row in dataframe.iterrows():

            # On récupère les valeurs à partir des colonnes
            idIndicatorGroup = row['SC_Group_ID']  # --> la colonne 1 = idIndicator
            # descIndicatorGroup = row['SC_Group_Desc']
            idCommodityGroup = row['SC_GroupCommod_ID']
            # descCommodityGroup = row['SC_GroupCommod_Desc']
            idGeography = row['SC_Geography_ID']
            # sortOrder = row['SortOrder']
            descGeography = row['SC_GeographyIndented_Desc']
            idCommodity = row['SC_Commodity_ID']
            descCommodity = row['SC_Commodity_Desc']
            idIndicator = row['SC_Attribute_ID']
            # descIndicator = row['SC_Attribue_Desc']
            idUnit = row['SC_Unit_ID']
            # descUnit = row['SC_Unit_Desc']
            idYear = row['Year_ID']
            idFrequency = row['SC_Frequency_ID']
            descFrequency = row['SC_Frequency_Desc']
            idTimePeriod = row['TimePeriod_ID']
            descTimePeriod = row['TimePeriod_Desc']
            amount = row['Amount']

            # Ici on réalise les create, c'est une ébauche ici
            if idUnit in [1, 3, 17, 18]:  # id correspondant aux volumes
                unit = FoodCropFactory.createVolume(FoodCropFactory.self, idUnit)
            elif idUnit in [2, 10, 44]:
                unit = FoodCropFactory.createSurface(FoodCropFactory.self, idUnit)
            elif idUnit in [7, 8, 9, 41]:
                unit = FoodCropFactory.createWeight(FoodCropFactory.self, idUnit, 1000) #le multiplier??? --> plusieurs cas
            elif idUnit in [4, 5, 12, 14, 31]:
                unit = FoodCropFactory.createPrice(FoodCropFactory.self, idUnit)
            elif idUnit in [16, 46]:
                unit = FoodCropFactory.createCount(FoodCropFactory.self, idUnit, "exemple") #le what??? --> plusieurs cas
            elif idUnit in [6, 11, 13, 45]:
                unit = FoodCropFactory.createRatio(FoodCropFactory.self, idUnit)
            # elif idUnit in [15]:
            # unit = FoodCropFactory.createDate(idUnit)
            else:
                unit= null # nécessaire sinon erreur pour créer indicator

            indicator = FoodCropFactory.createIndicator(FoodCropFactory.self, idIndicator, idFrequency, descFrequency, descGeography,
                                                        idIndicatorGroup, unit)
            commodity = FoodCropFactory.createCommodity(FoodCropFactory.self, CommodityGroup, idCommodity, descCommodity) #CommodityGroup est de type int / à changer en int
            measurement = FoodCropFactory.createMeasurement(FoodCropFactory.self, index, idYear, amount, idTimePeriod, descTimePeriod,
                                                            commodity, indicator)


            # Ici on indexe les measurements
            # dictionnaire unit
            if unit not in self.dicoUnit:  # On a pas encore de mesures pour cette valeur de unit, on initialise une liste vide
                self.dicoUnit[unit] = list()

            self.dicoUnit[unit].append(measurement)  # On ajoute notre mesure

            # dictionnaire commodity group
            if idCommodityGroup not in self.dicoCommodityGroup:
                self.dicoCommodityGroup[idCommodityGroup] = list()

            self.dicoCommodityGroup[idCommodityGroup].append(measurement)

            # dictionnaire indicator group
            if idIndicatorGroup not in self.dicoIndicatorGroup:
                self.dicoIndicatorGroup[idIndicatorGroup] = list()

            self.dicoIndicatorGroup[idIndicatorGroup].append(measurement)

            # dictionnaire localisation géographique
            if idGeography not in self.dicoLocGeo:
                self.dicoLocGeo[idGeography] = list()

            self.dicoLocGeo[idGeography].append(measurement)


    def findMeasurements(self, commodityType: CommodityType = nil, indicatorGroup: IndicatorGroup = nil,
                         geographicalLocation: str = nil, unit: Unit = nil) -> List[Measurement]:
        listCommodity = [] #liste des id des mesures dont le commodity group correspond à celui recherché
        listIndicator = []
        listGeog = []
        listUnit = []
        liste_mesures = list()
        liste1 = dico.Commoditygroup(CG) #comme listCommodity mais avec  les mesures
        for element in liste1:
            list1.append(element.id)
            liste2 = dico.IndicatorGroup(IG)
        for element in liste2:
            list2.append(element.id)
        for element in list1:
            if element is in list2:
                list3.append(element)
                ...
        for element in list3:
            liste_mesures.append(dataframe.ligne(element))
        return liste_mesures

        pass
    #renvoie une Liste de Measurement
    #si argument = corn, alors on cherche dans le dictionnaire la liste qui correspond
    #dans la liste trouvée, quel groupe en commun

    #ou alors faire une liste par arguments et après les croiser simplement












"""

##DICTIONNAIRE UNIT
#affiche le nom de chaque colonne
for idx, column in enumerate(dataframe.columns):
    print(idx,column)

#extraction d'une colonne
dataframe['SC_Unit_Desc']

#extraction de deux colonnes
dataframe[['SC_Unit_ID','SC_Unit_Desc']]

#combien de valeurs différentes
dataframe[['SC_Unit_ID','SC_Unit_Desc']].nunique()

#sans les doublons, 1 attribut
dataframe['SC_Unit_ID'].unique()
dataframe['SC_Unit_Desc'].unique()

#une ligne du dictionnaire
[dataframe['SC_Unit_ID'].unique()[3],dataframe['SC_Unit_Desc'].unique()[3]]

#création du dictionnaire Unit
dico_Unit = dict()
for i in range(dataframe['SC_Unit_ID'].nunique()) :
    dico_Unit[dataframe['SC_Unit_Desc'].unique()[i]] = dataframe['SC_Unit_ID'].unique()[i]


##DICTIONNAIRE COMMODITY
dico_Commodity = dict()
for i in range(dataframe['SC_Commodity_ID'].nunique()) :
    dico_Commodity[dataframe['SC_Commodity_Desc'].unique()[i]] = dataframe['SC_Commodity_ID'].unique()[i]

##DICTIONNAIRE INDICATOR
dico_Indicator = dict()
for i in range(dataframe['SC_Attribute_ID'].nunique()) :
    dico_Indicator[dataframe['SC_Attribute_Desc'].unique()[i]] = dataframe['SC_Attribute_ID'].unique()[i]
    
##

"""
