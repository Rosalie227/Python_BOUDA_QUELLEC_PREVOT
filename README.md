# Python_crew
Rapport du Projet Python

→ README de la forge Git


I - Description de l’environnement de développement :

Lors de notre travail sur ce projet, nous avons utilisé la version 3.8 de Python que nous avons installée à partir d’Anaconda. Ce dernier est une plateforme de distribution en open-source des langages de programmation Python et R. 
Rosalie ayant un Mac (système d’exploitation MacOS 10.13.6), et Charlotte et Rémi étant sous Windows10, nous avons dû chacun installer différemment cette plateforme. La version d’Anaconda installée (Anaconda3-2020.07) nous a permis de travailler avec la version 3.8 de Python.
L’IDE (Integrated Development Environment) que nous avons choisi d’utiliser est celui conseillé, à savoir PyCharm. La version que nous avons téléchargée est la version professionnelle 2020.2.3 que nous avons récupérée depuis JetBrains après création d’un compte.


II  - Instructions pour faire tourner le programme :

	dataset = FoodCropsDataset()
	dataset.load('/Users/Moi/Downloads/Feed Grains.csv') //lien vers le document

	results = dataset.findMeasurements(commodityType=‘choix1’, indicatorGroup=‘choix2’, geographicalLocation=‘choix3’, unit=‘choix4’)

	for result in results:
  		print(result.describe())


III - Description de la répartition des tâches:

Installation de l’environnement de développement ;
Création d’un projet GitHub afin de regrouper les avancements de chacun ;
Lecture du sujet chacun de son côté puis mise en commun des informations ;
Chaque personne s’est occupé de créer certaines classes (le corps des classes tel qu’indiqué dans le diagramme de classes, d’abord sans compléter les méthodes) ;
Concertation afin de comprendre le lien entre les classes et comment compléter les méthodes ;
Répartition des différentes unités dans les sous-classes ;
Travail en simultané sur la complétion des méthodes du code par un partage d’écran d’un membre de l’équipe ;
Tests réalisés sur plusieurs ordinateurs pour comparer les erreurs apparues ;
Un membre s’est occupé de bien finaliser l’apparence/la clarté du code, les deux autres ont rédigé le rapport ;
Relecture et correction du rapport par tout le groupe.


IV - Problèmes rencontrés :

Emploi des self : nous avons eu des soucis de syntaxe vis-à-vis du self, notamment dans la classe FoodCropFactory.
Utilisation d’une énumération : il nous a fallu un peu de temps pour comprendre comment sélectionner le nom ou la valeur d’un élément d’une énumération.
Méthodes describe() : nous ne savions pas bien quoi mettre dans les différentes méthodes describe(), c’est pourquoi nous avons d’abord traité le O4. avant le O3. Nous avons ensuite mieux compris le rôle des describe() (~ toString) et avons pu compléter ces méthodes.
La méthode load(datasetPath) : initialement, nous n’avions pas bien saisi l’utilité des différents dictionnaires. Nous pensions que createMeasurement(...) devait créer la liste des mesures dans une liste.
Nous avons eu beaucoup de mal à comprendre le terme instancier qui ne nous était pas familier.
Nous avons eu du mal à répartir les différentes unités dans les sous-classes (volumes, ratio etc.). Certaines unités n’étaient pas claires et nous les avons attribuées à certaines sous-classes sans certitude (ex: metric tons/hectare). De plus, nous avons créé une nouvelle sous-classe qui n’était pas dans le sujet : Date (pour pouvoir ranger l’index).
Le fait de ne pas pouvoir travailler en présentiel a été un obstacle à la réalisation de ce projet. Nous avons dû nous adapter (partage d’écran notamment).
Rémi a eu du mal à installer Anaconda malgré les conseils de M.XU (réinstallation plusieurs fois, les fichiers/bibliothèques n’étaient pas correctement installés).
