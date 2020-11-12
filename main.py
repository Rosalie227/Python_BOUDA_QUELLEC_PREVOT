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
class Unit(Describable):  # j'ai rajouté ABC pour dire que c'est une classe abstraite
    id: int
    name: str

    def __init__(self, id: int, name: str):
        super().__init__()
        self.id = id
        self.name = name

    def describe(self):
        pass


class Volume(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Volume')

    def describe(self) -> str:
        return "Cette unité est un " + self.name + " avec pour id = "+str(self.id)


class Surface(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Surface')

    def describe(self) -> str:
        return "Cette unité est une " + self.name + " avec pour id = "+str(self.id)


class Price(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Price')

    def describe(self) -> str:
        return "Cette unité est un " + self.name + " avec pour id = "+str(self.id)


class Count(Unit):
    __what: str  # le underscore signifie que l'attribue est privé

    def __init__(self, id: int, what: str):
        super().__init__(id, name='Count')
        self.__what = what  # attribut _what prend valeur what

    def describe(self) -> str:
        return "Cette unité est un " + self.name + " qui correspond à des " + self.__what + " avec pour id = " + str(self.id)


class Weight(Unit):
    __multiplier: float  # attribut privé

    def __init__(self, id: int, multiplier: float):
        super().__init__(id, name='Weight')
        self.__multiplier = multiplier  # attribut _multiplier prend valeur multiplier

    def describe(self) -> str:
        return "Cette unité est un " + self.name + " multiplié par " + str(self.__multiplier) + " avec pour id = " + str(self.id)


class Ratio(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Ratio')

    def describe(self) -> str:
        return "Cette unité est un " + self.name + " avec pour id = "+str(self.id)


class Date(Unit):
    def __init__(self, id: int):
        super().__init__(id, name='Date')

    def describe(self) -> str:
        return "Cette unité est une " + self.name + " avec pour id = "+str(self.id)


class Indicator(Describable):
    idIndicator: int    # attribut public
    __frequency: int
    __frequencyDesc: str
    __geogLocation: str
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

    def describe(self) -> str:
        chaine = "Cet indicateur est le " + str(self.idIndicator) + "du groupe : " + self.__indicatorGroup.name + \
                 " de fréquence correspondante " + str(self.__frequency) + " : " + self.__frequencyDesc + \
                 "et de localisation géographique : " + self.__geogLocation + ". Son unité est " + unit.describe()
        return chaine


class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 1 # garder ces numéros ou les changer en fonction de la database
    SUPPLY_AND_USE = 2
    PRICES = 3
    FEED_PRICE_RATIOS = 4
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

    def describe(self) -> str:
        chaine = "Cette culture vivrière est " + str(self.id) + " : " + self.__name + " du groupe : " + self.__group.name
        return chaine


class CommodityGroup(Enum):  # idem, garder les mêmes chiffres ou non
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

    def describe(self) -> str:
        chaine = "Cette mesure de valeur " + str(self.__value) + " est la mesure n°" + str(self.__id) + " datant de l'année " + str(self.__year) + \
                 " au mois de " + str(self.__timePeriodId) + " " + self.__timePeriodDescr + \
                 " correspondant à la culture vivrière : " + self.__commodity.describe() + " et à l'indicateur : " + self.__indicator.describe()
        return chaine


# FoodCropFactory
class FoodCropFactory:

    def __init__(self):
        super().__init__()
        self.units_registry = {}
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

    def createCommodity(self, group: int, id: int, name: str) -> Commodity:
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
            instance = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)   # erreur de type
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
    def __init__(self):
        super().__init__()
        self.dicoCommodityGroup = {}
        self.dicoIndicatorGroup = {}
        self.dicoLocGeo = {}
        self.dicoUnit = {}

    def load(self, datasetPath: str):
        #datasetPath = 'C:\\Users\\charl\\Documents\\2A EMA\\poo\\Projet Python\\FeedGrains.csv'
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
            elif idUnit in [41]:
                unit = FoodCropFactory.createWeight(FoodCropFactory.self, idUnit, 1) #différents cas en f° de multiplier
            elif idUnit in [7, 9]:
                unit = FoodCropFactory.createWeight(FoodCropFactory.self, idUnit, 1000)
            elif idUnit in [8]:
                unit = FoodCropFactory.createWeight(FoodCropFactory.self, idUnit, 1000000)
            elif idUnit in [4, 5, 12, 14, 31]:
                unit = FoodCropFactory.createPrice(FoodCropFactory.self, idUnit)
            elif idUnit in [16]:
                unit = FoodCropFactory.createCount(FoodCropFactory.self, idUnit, "wagons") #différents cas en f° de what
            elif idUnit in [46]:
                unit = FoodCropFactory.createCount(FoodCropFactory.self, idUnit, "millions d'unités animales")
            elif idUnit in [6, 11, 13, 45]:
                unit = FoodCropFactory.createRatio(FoodCropFactory.self, idUnit)
            elif idUnit in [15]:
                unit = FoodCropFactory.createDate(FoodCropFactory.self, idUnit)
            else:
                unit= None # nécessaire sinon erreur pour créer indicator

            indicator = FoodCropFactory.createIndicator(FoodCropFactory.self, idIndicator, idFrequency, descFrequency, descGeography,
                                                        idIndicatorGroup, unit)
            commodity = FoodCropFactory.createCommodity(FoodCropFactory.self, idCommodityGroup, idCommodity, descCommodity) #CommodityGroup est de type int / à changer en int
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


    def findMeasurements(self, commodityType: CommodityType = None, indicatorGroup: IndicatorGroup = None,
                         geographicalLocation: str = None, unit: Unit = None) -> List[Measurement]:
        liste_mesures = list()
        liste_toutes_les_mesures = list()
        for cle , valeur in self.dicoCommodityGroup.items():   #On aurait pu prendre n'importe lequel des dictionnaires
            liste_toutes_les_mesures += valeur                 #On ajoute chaque "morceau" de la liste des mesures qui sont séparées dans le dico
        if commodityType is None:
            liste_mesures_Commodity = liste_toutes_les_mesures #Pour avoir toutes les mesures et pouvoir croiser
        else :
            liste_mesures_Commodity = self.dicoCommodityGroup[commodityType] #On affecte la liste des mesures qui ont pour CommodityGroup celui recherché
        if indicatorGroup is None:
            liste_mesures_Indicator = liste_toutes_les_mesures
        else :
            liste_mesures_Indicator = self.dicoIndicatorGroup[indicatorGroup]
        if geographicalLocation is None:
            liste_mesures_Geogloc = liste_toutes_les_mesures
        else :
            liste_mesures_Geogloc = self.dicoLocGeo[geographicalLocation]
        if unit is None:
            liste_mesures_Unit = liste_toutes_les_mesures
        else :
            liste_mesures_Unit = self.dicoUnit[unit]
        for element in liste_mesures_Commodity:              #On aurait pu commencer par n'importe laquelle des 4 listes
            if element in liste_mesures_Indicator and element in liste_mesures_Geogloc and element in liste_mesures_Unit : #Si la mesure correspond à toutes les critères
                liste_mesures.append(element)                                                                              #on l'ajoute à la liste à renvoyer
        return liste_mesures




##MAIN
dataset = FoodCropDataset()
dataset.load('C:\\Users\\charl\\Documents\\2A EMA\\poo\\Projet Python\\FeedGrains.csv')

results = dataset.find_measurement(self, commodityType = None, indicatorGroup = None,
                         geographicalLocation = None, unit = None)

for result in results:
    print(result.describe())





