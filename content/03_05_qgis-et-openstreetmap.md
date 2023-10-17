
## III.5 QGIS et OpenStreetMap

* [Qu'est-ce qu'OpenStreetMap ?](#III51 "#III51")
* [Visualiser un fonds OpenStreetMap](#III52 "#III52")
* [Télécharger des données OpenStreetMap](#III53 "#III53")
* [Représenter des données OpenStreetMap](#III54 "#III54")
* [Charger des données OpenStreetMap à partir de QGIS](#III55 "#III55")

### Qu'est-ce qu'OpenStreetMap ?

[OpenStreetMap ou OSM](http://www.openstreetmap.org "http://www.openstreetmap.org") est un projet qui a pour but de constituer une base de données géographiques libre du monde. A l'instar de [Wikipédia](https://fr.wikipedia.org "https://fr.wikipedia.org"), tout un chacun peut participer et enrichir le projet. On peut donc visualiser, réutiliser et même après inscription modifier gratuitement les données.

La partie la plus connue du projet est peut-être la visualisation des données OSM sous forme de [carte](http://www.openstreetmap.org/#map=19/44.79461/-0.61780 "http://www.openstreetmap.org/#map=19/44.79461/-0.61780") ; mais OSM est avant tout un ensemble de [données](https://www.openstreetmap.org/way/226888023 "https://www.openstreetmap.org/way/226888023") géographiques, utilisables entre autres dans un logiciel SIG.

[![OpenStreetMap : extrait de carte](illustrations/3_4_carte.jpg)](illustrations/3_4_carte.jpg "illustrations/3_4_carte.jpg")
[![OpenStreetMap : extrait de carte avec les données en bleu](illustrations/3_4_donnees.jpg)](illustrations/3_4_donnees.jpg "illustrations/3_4_donnees.jpg")
Sous la carte... les données !

Les attributs des données OSM sont des paires **clé=valeur** (key=value). Un élément peut par exemple être caractérisé par **l'attribut** (tag) **waterway=river** pour indiquer qu'il s'agit d'un cours d'eau de type rivière. La clé est ici waterway et la valeur river. Un élément peut être caractérisé par plusieurs attributs (plusieurs paires clé=valeur).

Il existe plusieurs valeurs possibles pour chaque clé, la clé **waterway** peut par exemple avoir comme valeur **river** (rivière), **stream** (ruisseau), **canal**... Retrouvez [ici](http://wiki.openstreetmap.org/wiki/FR:%C3%89l%C3%A9ments_cartographiques "http://wiki.openstreetmap.org/wiki/FR:%C3%89l%C3%A9ments_cartographiques") la liste des clés et des valeurs couramment utilisées.

Nous allons découvrir ici différentes manières pour non seulement visualiser un fonds OSM, mais également pour utiliser les données OSM dans QGIS. Il est possible de télécharger ces données à partir de différents sites pour ensuite les ajouter à QGIS, mais aussi de les charger directement dans QGIS.

### Visualiser un fonds OpenStreetMap

Il s'agira ici de simplement visualiser les données OSM comme un fonds raster, c'est-à-dire une image non modifiable. OSM étant une base de données, il est possible de représenter ces données comme on le souhaite ; plusieurs organismes proposent ainsi leur représentation des données OSM. Ces représentations peuvent avoir des objectifs différents : servir de fonds de carte discret, représenter les itinéraires cyclables, les données utiles pour les organisations humanitaires...

Il est possible d'afficher un fonds OpenStreetMap, comme décrit précédemment, soit [via l'explorateur avec un serveur de tuiles](03_04_fonds_carte.php#III42 "03_04_fonds_carte.php#III42"), soit [via l'extension QuickMapServices](03_04_fonds_carte.php#III43 "03_04_fonds_carte.php#III43").

Si vous choisissez la première méthode, voici comment ajouter de nombreux fonds utilisant les données OSM :

Dans un navigateur internet, rendez-vous dans [la page du wiki OSM dédiée aux serveurs de tuiles raster](https://wiki.openstreetmap.org/wiki/Tile_servers "https://wiki.openstreetmap.org/wiki/Tile_servers") : cette page liste les adresses des fonds de carte utilisant les données OSM accessibles en ligne.

Ici, nous allons ajouter le fonds **Stamen Toner** en noir et blanc.

[![page du wiki OSM sur les serveurs de tuiles, ligne correspondant au fonds Stamen Toner](illustrations/3_5_stamen_toner.jpg)](illustrations/3_5_stamen_toner.jpg "illustrations/3_5_stamen_toner.jpg")

Copiez l'url du serveur : **<https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.jpg>**

Dans QGIS, panneau explorateur, clic-droit sur XYZ Tiles → Nouvelle connexion...

[![Fenêtre de nouvelle connexion à un serveur de tuiles](illustrations/3_5_stamen_connexion.jpg)](illustrations/3_5_stamen_connexion.jpg "illustrations/3_5_stamen_connexion.jpg")

* Nom : il s'agit du nom qui apparaîtra dans le panneau explorateur, vous pouvez taper par exemple **Stamen Toner**
* URL : collez l'URL que vous avez préalablement copiée : **<https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.jpg>**

Si l'URL contient le caractère **$**, il faut le supprimer, par exemple http://c.tile.stamen.com/watercolor/${z}/${x}/${y}.jpg devient <http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg>.

Laissez les valeurs par défaut pour les autres paramètres, cliquez sur OK.

Le fonds Stamen Toner apparaît maintenant avec les autres fonds dans la rubrique XYZ Tiles.

[![panneau explorateur, rubrique XYZ Tiles : le fonds Stamen Toner apparaît avec les autres](illustrations/3_5_stamen_xyz.jpg)](illustrations/3_5_stamen_xyz.jpg "illustrations/3_5_stamen_xyz.jpg")

Double-cliquez pour l'ajouter :

[![Aperçu du fonds Stamen Toner](illustrations/3_5_stamen_visu.jpg)](illustrations/3_5_stamen_visu.jpg "illustrations/3_5_stamen_visu.jpg")

### Télécharger des données OpenStreetMap

Il existe plusieurs possibilités pour [télécharger des données OSM](http://wiki.openstreetmap.org/wiki/Downloading_data "http://wiki.openstreetmap.org/wiki/Downloading_data"), notamment [au format Shapefile](http://wiki.openstreetmap.org/wiki/Shapefiles#Download_shapefiles "http://wiki.openstreetmap.org/wiki/Shapefiles#Download_shapefiles").

Nous utiliserons ici les données créées par [Geofabrik](http://www.geofabrik.de/ "http://www.geofabrik.de/"), une société allemande spécialisée dans les services autour d'OpenStreetMap. Les données sont extraites d'OpenStreetMap et mises à jour quotidiennement. Il est possible de les télécharger par continent, sous-région, pays et parfois région au sein du pays.

Dans un navigateur internet, rendez-vous sur [http://download.geofabrik.de/](http://download.geofabrik.de/ "http://download.geofabrik.de/").

Il est possible de télécharger les données par continent, pays, et parfois région. Nous allons ici télécharger les données du Suriname en Amérique du Sud.

Dans la colonne **Sub-Region**, cliquez sur **South America**, puis sur téléchargez les données au format shapefile pour le **Suriname**.

[![lien pour télécharger les données du Suriname au format SHP sur Geofabrik](illustrations/3_5_geofabrik_southamerica.jpg)](illustrations/3_5_geofabrik_southamerica.jpg "illustrations/3_5_geofabrik_southamerica.jpg")

[![lien pour télécharger les données du Suriname au format SHP sur Geofabrik](illustrations/3_5_geofabrik_suriname.jpg)](illustrations/3_5_geofabrik_suriname.jpg "illustrations/3_5_geofabrik_suriname.jpg")

Au cas où le téléchargement échouerait, ces données sont également disponibles [avec les données de la partie III](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip").

Enregistrer le fichier sur votre ordinateur, décompressez le fichier ZIP obtenu dans votre répertoire de travail : vous obtenez une série de couches au format Shapefile.

Que contiennent ces données ? Pour le savoir, cliquez sur le lien [Format description PDF](http://download.geofabrik.de/osm-data-in-gis-formats-free.pdf "http://download.geofabrik.de/osm-data-in-gis-formats-free.pdf") disponible en cliquant sur **Suriname**
[à partir de la page où vous avez téléchargé les données

![Page geofabrik Suriname avec le lien vers le PDF des métadonnées entouré en rouge](illustrations/3_5_lien_pdf_geofabrik.jpg)](#thumb "#thumb").

Notez que les noms de couches correspondent aux clés des attributs OSM. Par exemple, la couche *gis.osm_waterways_free_1* regroupe les éléments ayant la clé [waterway](http://wiki.openstreetmap.org/wiki/FR:Key:waterway "http://wiki.openstreetmap.org/wiki/FR:Key:waterway").

Dans un nouveau projet QGIS, ajoutez ces données. Ouvrez la table attributaire de la couche *gis.osm_waterways_free_1*.

Les valeurs du champ **fclass** correspondent aux différentes valeurs prises par la clé de la couche pour chaque élément. On trouve par exemple les valeurs river, stream, canal et drain.

### Représenter des données OpenStreetMap

Les données OpenStreetMap ajoutées dans QGIS, comme toute autre donnée, ont un style « par défaut », ne convenant pas pour une carte. Nous allons voir ici comment représenter ces données pour obtenir quelque chose de similaire à ceci :

[![Exemple de données OSM stylées, grande échelle](illustrations/3_5_style_resultat.jpg)](illustrations/3_5_style_resultat.jpg "illustrations/3_5_style_resultat.jpg")

Chargez dans QGIS les couches GeoFabrik suivantes :

* qgis.osm_roads_free.1
* qgis.osm_buildings_a_free.1
* qgis.osm_railways_free.1
* qgis.osm_waterways_free.1
* qgis.osm_water_a_free.1
* qgis.osm_natural_a_free.1
* qgis.osm_landuse_a_free.1

Une dernière couche sera nécessaire : ajoutez également la couche *[land_polygons_suriname](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")*.

Dans QGIS, le style d'une couche est enregistré dans le projet. Il est également possible de créer des fichiers de style, au format **QML** (fichier de style QGIS, propre au logiciel) ou **SLD** (Style Layer Descriptor, utilisé plus largement en cartographie web).

Nous allons ici charger pour chaque couche un fichier de style QML approprié. Ces fichiers ont été élaborés à partir de ceux créés par Charley Glynn et disponibles sur [https://github.com/charleyglynn/OSM-Shapefile-QGIS-stylesheets](https://github.com/charleyglynn/OSM-Shapefile-QGIS-stylesheets "https://github.com/charleyglynn/OSM-Shapefile-QGIS-stylesheets").

Ces fichiers de style sont adaptés pour un SCR projeté, car certaines taille de symboles sont définies en suivant les unités de la carte et adaptés pour des unités métriques et non en degrés. La première étape consistera donc à adopter un SCR projeté.

[Modifiez le SCR du projet](02_04_changer_systeme.php#II41 "02_04_changer_systeme.php#II41") pour choisir par exemple le SCR World_Robinson (code EPSG 54030), et activez la projection à la volée.

Modifiez l'ordre des couches pour obtenir ceci :

[![Ordre des couches OSM](illustrations/3_5_ordre_couches.jpg)](illustrations/3_5_ordre_couches.jpg "illustrations/3_5_ordre_couches.jpg")

Ouvrez la fenêtre **Propriétés** de la couche *gis.osm_roads_free_1*, rubrique **Symbologie** :

[![Charger un style](illustrations/3_5_charger_style.jpg)](illustrations/3_5_charger_style.jpg "illustrations/3_5_charger_style.jpg")

En bas de la fenêtre, cliquez sur la liste déroulante **Style** puis sur **Charger le style**.

[![Sélectionner un style depuis un fichier](illustrations/3_5_charger_style_fenetre.jpg)](illustrations/3_5_charger_style_fenetre.jpg "illustrations/3_5_charger_style_fenetre.jpg")

Dans la fenêtre qui s'affiche :

* sélectionnez **depuis un fichier** dans la liste déroulante
* Fichier : cliquez sur le bouton **...** et sélectionnez le fichier de style **[roads.qml](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")** situé dans le dossier **TutoQGIS_03_RechercheDonnees/legendes**.
* Catégories : laissez les valeurs par défaut
* Cliquez sur **Charger le style**

Cliquez ensuite sur **OK** pour fermer la fenêtre des propriétés.

Zoomez et dézoomez : le style change suivant le niveau de zoom.

Procédez de manière similaire pour chacune des couches, en choisissant à chaque fois le fichier de style approprié.

Pour finir, donnez un fond bleu à votre carte : **menu Projet → Propriétés... → rubrique Général, Paramètres généraux (en haut)** : cliquez sur la couleur à droite de **Couleur d'arrière-plan**.

[![Propriétés du projet, Général : modification de la couleur d'arrière-plan](illustrations/3_5_modif_couleur_fond.jpg)](illustrations/3_5_modif_couleur_fond.jpg "illustrations/3_5_modif_couleur_fond.jpg")

Dans la boîte de dialogue qui s'affiche alors, choisissez une couleur pour la mer, par exemple dans l'exemple ci-dessous **R 184 V 217 B 247**.

[![Choix d'une couleur RVB](illustrations/3_5_couleur_rvb.jpg)](illustrations/3_5_couleur_rvb.jpg "illustrations/3_5_couleur_rvb.jpg")

Notez qu'une manipulation équivalente peut être effectuée dans le [mode mise en page](10_02_mise_en_page.php#X22 "10_02_mise_en_page.php#X22"), sans changer la couleur de fond dans QGIS.

[![Exemple de données OSM stylées, petite échelle](illustrations/3_5_style_resultat_2.jpg)](illustrations/3_5_style_resultat_2.jpg "illustrations/3_5_style_resultat_2.jpg")

Vous pouvez ensuite si vous le désirez modifier le style des couches pour créer votre propre version. Pour enregistrer un fichier de style QML, procédez comme pour charger un style, mais choisissez **Enregistrer le style**.

### Charger des données OpenStreetMap à partir de QGIS

Nous allons utiliser ici l'extension [QuickOSM](https://github.com/3liz/QuickOSM "https://github.com/3liz/QuickOSM") pour charger des données OpenStreetMap directement dans QGIS.

Cette extension permet le téléchargement de données OSM sous forme de couches temporaires, pour l'emprise de votre choix.

Elle offre par rapport aux solutions précédentes une possibilité supplémentaire : **choisir la clé et les valeurs voulues**. Vous pouvez ainsi télécharger uniquement les cours d'eau de type rivière pour une zone.

Ouvrez un nouveau projet QGIS. Ajoutez la couche *[ne_10m_admin_0_countries](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")* située dans le dossier **TutoQGIS_03_RechercheDonnees/donnees**. Zoomez sur le Suriname.

Pour **installer l'extension QuickOSM** (cette étape nécessite une connexion internet) :

* rendez-vous dans le **menu Extensions → Installer/Gérer les extensions**, rubrique **Toutes**
* tapez **quickosm** dans la barre de recherche en haut
* cliquez sur le nom de l'extension puis sur le bouton **Installer l'extension** en bas à droite
* Fermez la fenêtre du gestionnaire d'extension.

Pour accéder à QuickOSM : **menu Vecteur → Quick OSM → QuickOSM**. La fenêtre suivante s'ouvre :

[![Fenêtre de QuickOSM, choix des options](illustrations/3_5_quickosm_fenetre.jpg)](illustrations/3_5_quickosm_fenetre.jpg "illustrations/3_5_quickosm_fenetre.jpg")

Dans la rubrique **Requête rapide** :

* Choisissez la clé **waterway** puis la valeur **river** pour ne récupérer que les cours d'eau de type rivière
* Dans la liste déroulante **Dans**, sélectionnez l'option **Emprise du canevas** pour limiter le volume de données à charger à la zone visible dans QGIS
* Cliquez enfin sur le bouton **Exécuter**.

Patientez (plus la zone visible dans QGIS est grande, plus c'est long !)... Les données sont chargées et affichées :

[![Aperçu des données récupérées avec OSM : rivières du Suriname](illustrations/3_5_quickosm_resultat.jpg)](illustrations/3_5_quickosm_resultat.jpg "illustrations/3_5_quickosm_resultat.jpg")

Ces données sont temporaires : pour les sauvegarder, clic droit sur la couche → Exporter → Sauvegarder les entités sous...

Pour savoir où sont stockées les données temporaires : propriétés de la couche, rubrique Information, ou bien dans l'infobulle qui s'affiche en survolant le nom de la couche.

Nous avons vu ici quelques méthodes pour accéder aux données OSM dans QGIS, mais il en existe d'autres !

[chapitre précédent](03_04_fonds_carte.php "03_04_fonds_carte.php")
[partie IV : géoréférencement](04_00_georeferencement.php "04_00_georeferencement.php")

[haut de page](#wrap "#wrap")
