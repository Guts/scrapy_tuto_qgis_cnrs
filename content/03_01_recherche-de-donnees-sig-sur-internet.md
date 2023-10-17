
## III.1 Recherche de données SIG sur internet


* [Données nationales pour la France](#III11 "#III11")
	+ [Avec l'IGN](#III11a "#III11a")
	+ [Avec geo.data.gouv.fr](#III11b "#III11b")
* [Données mondiales](#III12 "#III12")
	+ [Avec Natural Earth](#III12a "#III12a")
	+ [Avec les données SRTM](#III12b "#III12b")
* [Et tout le reste ?](#III13 "#III13")




Il est possible de trouver sur internet des **données déjà géoréférencées, c'est-à-dire possédant déjà des coordonnées, donc directement utilisables dans un SIG**. Ces données peuvent être vecteur ou raster.


Dans le cas de **données vecteur**, le format le plus courant est sans doute le shapefile ; on trouvera aussi des données dans d'autres formats, par exemple GeoPackage, GeoJSON, KML...


Dans le cas de **données raster**, on pourra trouver par exemple des données au format geotiff (TIF géoréférencé, c'est-à-dire avec des coordonnées lui permettant de se superposer correctement à d'autres couches).


Parfois, on ne trouvera que des **données non géoréférencées** (carte papier par exemple, ou simple image trouvée sur internet). Ce cas sera traité dans la [partie 4 : géoréférencement](04_00_georeferencement.php "04_00_georeferencement.php").


Cette partie se borne à donner quelques exemples de sites permettant le téléchargement de données SIG. Il en existe beaucoup d'autres !


Ne vous offusquez pas de ne pas voir ici les **données OpenStreetMap** : il existe [une partie qui leur est spécialement dédiée !](03_05_donnees_osm.php "03_05_donnees_osm.php")


### Données nationales pour la France


#### Avec l'IGN


L'IGN (Institut National de l'Information Géographique et Forestière) diffuse gratuitement la plupart de ses données ici : [https://geoservices.ign.fr/catalogue](https://geoservices.ign.fr/catalogue "https://geoservices.ign.fr/catalogue").


Si vous êtes étudiant ou bien si vous travaillez dans un laboratoire de recherche, il existe peut-être entre votre structure et l'IGN une convention recherche et enseignement vous donnant accès à plus de données !


Nous allons ici télécharger les **communes de la Guyane**.



Sur la page internet [https://geoservices.ign.fr/catalogue](https://geoservices.ign.fr/catalogue "https://geoservices.ign.fr/catalogue"), cliquez sur [ADMIN-EXPRESS](https://geoservices.ign.fr/adminexpress "https://geoservices.ign.fr/adminexpress").


La page listant beaucoup de données, vous pouvez faire une recherche sur le terme **admin** avec la fonction **rechercher** de votre navigateur (ou le raccourci clavier **ctrl + F**). Vous pouvez aussi filtrer les données sur **Données/services** puis **Bases de données au format vectoriel**.



[![page de téléchargement des données IGN](illustrations/3_1_ign_telechargement.jpg)](illustrations/3_1_ign_telechargement.jpg "illustrations/3_1_ign_telechargement.jpg")


La base ADMIN EXPRESS contient des couches de régions, départements, arrondissements, EPCI, communes et chef-lieux pour la France métropolitaine et ultra-marine. Elle remplace la base GEOFLA® qui n'est plus mise à jour et dont la dernière édition est celle de 2016.



Attention, le téléchargement de ces données peut être un peu long (environ 255 Mo pour la version de juin 2022), vous pouvez également utiliser directement la couche [*COMMUNE*](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip") disponible en téléchargement.


Téléchargez la dernière édition des données **ADMIN EXPRESS par territoire** (ici celle de juin 2022) :



[![page de téléchargement des données ADMIN EXPRESS (IGN)](illustrations/3_1_ign_telechargement_2.jpg)](illustrations/3_1_ign_telechargement_2.jpg "illustrations/3_1_ign_telechargement_2.jpg")

Vous pouvez également télécharger la version [COG (Code Officiel Géographique)](https://geoservices.ign.fr/ressources_documentaires/Espace_documentaire/BASES_VECTORIELLES/ADMIN_EXPRESS_COG/SE_ADMIN_EXPRESS_COG.pdf "https://geoservices.ign.fr/ressources_documentaires/Espace_documentaire/BASES_VECTORIELLES/ADMIN_EXPRESS_COG/SE_ADMIN_EXPRESS_COG.pdf") mais celle-ci est plus lourde.


Dézippez le fichier téléchargé (vous pouvez par exemple utiliser [7-zip](https://www.7-zip.org/ "https://www.7-zip.org/")).



Si le téléchargement échoue, cette couche est également accessible *[en téléchargement](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")*.



Une fois le fichier dézippé, vous pouvez constater qu'il contient une arborescence de dossiers complexe. Comment y voir plus clair ?


En commençant par les métadonnées ! Sur la page de téléchargement d'Admin Express, cliquez sur le bouton [Documentation](https://geoservices.ign.fr/documentation/donnees/vecteur/adminexpress "https://geoservices.ign.fr/documentation/donnees/vecteur/adminexpress") puis sur [ADMIN EXPRESS - Descriptif de contenu et de livraison](https://geoservices.ign.fr/sites/default/files/2021-11/DC_DL_ADMIN_EXPRESS_3-1_0.pdf "https://geoservices.ign.fr/sites/default/files/2021-11/DC_DL_ADMIN_EXPRESS_3-1_0.pdf"), ce qui ouvre un fichier PDF.


En parcourant ce PDF, vous en saurez plus sur les données que vous venez de télécharger. Vous y trouverez notamment page 7 la liste des différents SCR utilisés pour la France métropolitaine ainsi que pour l'Outre-Mer : le SCR utilisé pour la Guyane est le **RGF95 UTM 22, code EPSG 2972**.



Pour rappel, le but de l'exercice est ici d'afficher les communes de la Guyane, mais vous pouvez très bien décider de travailler sur un autre département !



La couche *COMMUNE* de la Guyane est donc située dans le sous-dossier **ADE_X-X_SHP_UTM22RGFG95_D973** où :


* **X-X** correspond à la version d'ADMIN EXPRESS téléchargée, par exemple 3-1
* **UTM22RGF95** correspond au SCR des données (voir plus haut)
* **D973** est le code du département


A partir de l'explorateur de fichiers de QGIS, ajoutez les communes de Guyane à la carte.



[![ajout de la couche de communes de Guyane via l'explorateur QGIS](illustrations/3_1_commune_guyane_explorateur.jpg)](illustrations/3_1_commune_guyane_explorateur.jpg "illustrations/3_1_commune_guyane_explorateur.jpg")

Selon votre version de QGIS et votre configuration, une fenêtre peut alors s'ouvrir pour vous demander quelle transformation vous souhaitez utiliser pour passer du SCR RGFG95 (utilisé en Guyane) et WGS84. Dans ce cas, choisissez la 1ère de ces transformations, normalement sélectionnée par défaut.



[![Choix de la transformation pour passer d'un SCR à un autre](illustrations/3_1_choix_transformation.jpg)](illustrations/3_1_choix_transformation.jpg "illustrations/3_1_choix_transformation.jpg")


Il semblerait que les 2 transformations disponibles ici aient les mêmes paramètres. Pour ajouter ou supprimer des transformations dans un projet : Propriétés du projet → rubrique Transformations.


Les [transformations](https://docs.qgis.org/3.10/fr/docs/user_manual/working_with_projections/working_with_projections.html#datum-transformations "https://docs.qgis.org/3.10/fr/docs/user_manual/working_with_projections/working_with_projections.html#datum-transformations") sont des formules mathématiques permettant la conversion des coordonnées d'un point d'un SCR à un autre. Il existe en effet parfois plusieurs transformations possibles pour passer d'un SCR à un autre !



Il est possible de paramétrer QGIS pour être informé ou non lorsqu'il existe plusieurs transformations disponibles entre 2 SCR :


**Menu Préférences → Options → rubrique Transformations** : vous pouvez décocher ou cocher la case **Demander de choisir la transformation de datum si plusieurs sont disponibles**.



[![Choix de l'option pour choisir soi-même ou non la transformation lorsque plusieurs sont disponibles](illustrations/3_1_options_transformations.jpg)](illustrations/3_1_options_transformations.jpg "illustrations/3_1_options_transformations.jpg")

Si cette case est décochée, QGIS choisira la transformation la plus précise : dans la plupart des cas, ce paramétrage est adapté.



Dans les données téléchargées sur le site de l'IGN se trouvent également les autres découpages administratifs pour la Guyane, ainsi que pour les autres territoires ultra-marins et la France métropolitaine.


Pour télécharger les données de l'IGN, vous pouvez également passer par [ign2map](https://geotribu.github.io/ign-fr-opendata-download-ui/index.html "https://geotribu.github.io/ign-fr-opendata-download-ui/index.html") (et profitez-en pour aller faire un tour sur l'excellent site [Geotribu](https://static.geotribu.fr/ "https://static.geotribu.fr/") !)


#### Avec geo.data.gouv.fr


Le site [https://geo.data.gouv.fr/fr/](https://geo.data.gouv.fr/fr/ "https://geo.data.gouv.fr/fr/") recense les jeux de données géographiques en accès libre pour la France. Nous allons utiliser ce site pour rechercher des données sur les hôpitaux en Guyane.



Dans la barre de recherche du site internet [https://geo.data.gouv.fr/fr/](https://geo.data.gouv.fr/fr/ "https://geo.data.gouv.fr/fr/"), tapez **hôpitaux guyane puis appuyez sur Entrée**.



[![recherche sur le site geo.data.gouv.fr](illustrations/3_1_geodatagouv_recherche.jpg)](illustrations/3_1_geodatagouv_recherche.jpg "illustrations/3_1_geodatagouv_recherche.jpg")

Vous obtenez plusieurs résultats. Ici, nous allons télécharger les données **Guyane - Finess cat1100 - Etablissements Hospitaliers**.



[![recherche sur le site geo.data.gouv.fr](illustrations/3_1_geodatagouv_recherche_2.jpg)](illustrations/3_1_geodatagouv_recherche_2.jpg "illustrations/3_1_geodatagouv_recherche_2.jpg")

Les métadonnées nous apprennent que ces données proviennent de la BD Adresse, datent de 2013 et ont été mises à jour il y a 3 ans.


Téléchargez ces données au format GeoJSON, en cliquant sur le bouton **GeoJSON** en bas à gauche de la fenêtre :



[![téléchargement au format geojson sur le site geo.data.gouv.fr](illustrations/3_1_geodatagouv_recherche_3.jpg)](illustrations/3_1_geodatagouv_recherche_3.jpg "illustrations/3_1_geodatagouv_recherche_3.jpg")

Si le téléchargement échoue, cette couche est également accessible en [téléchargement](donnees/TutoQGIS_03_RechercheDonnees.zip. "donnees/TutoQGIS_03_RechercheDonnees.zip.").


Ajoutez ensuite ces données à QGIS.



[![affichage des communes et des hôpitaux de Guyane](illustrations/3_1_guyane_communes_hopitaux.jpg)](illustrations/3_1_guyane_communes_hopitaux.jpg "illustrations/3_1_guyane_communes_hopitaux.jpg")


Si vous téléchargez les autres jeux de données résultant de la recherche sur "hôpitaux guyane", vous constaterez qu'ils présentent entre eux des différences de localisation et de données attributaires. Quel jeu de données vaut-il mieux utiliser ? Cette question est celle que vous vous poserez systématiquement à chaque nouveau projet, et y répondre peut parfois prendre un temps considérable et représenter un projet en soi ! La première piste de réponse est bien sûr d'aller voir les métadonnées, si elles sont disponibles.


### Données mondiales


#### Avec Natural Earth


[Natural Earth](https://www.naturalearthdata.com/ "https://www.naturalearthdata.com/") est un jeu de données cartographiques public mondial disponible à 3 échelles différentes. De nombreuses données sont disponibles, notamment les limites administratives, routes, cours d'eau et fonds raster.


Nous allons télécharger ici les **limites administratives des pays à petite échelle** (peu de niveau de détail).



Sur la page internet [https://www.naturalearthdata.com/downloads/](https://www.naturalearthdata.com/downloads/ "https://www.naturalearthdata.com/downloads/"), dans la rubrique **Small scale data 1:110m**, cliquez sur le bouton **Cultural**.



[![téléchargement des données Natural Earth](illustrations/3_1_naturalearth_telechargement.jpg)](illustrations/3_1_naturalearth_telechargement.jpg "illustrations/3_1_naturalearth_telechargement.jpg")

Ces données sont utilisables à l'échelle mondiale mais ne seront pas assez détaillées pour travailler à l'échelle d'un pays.


Sur la page suivante, dans **Admin 0 - Countries**, cliquez sur le bouton **Download countries**.



[![téléchargement des données Natural Earth](illustrations/3_1_naturalearth_telechargement_2.jpg)](illustrations/3_1_naturalearth_telechargement_2.jpg "illustrations/3_1_naturalearth_telechargement_2.jpg")

Si le téléchargement échoue, cette couche est également accessible *[en téléchargement](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")*.


Une fois le fichier téléchargé, placez-le dans votre dossier **TutoQGIS_03_RechercheDonnees/donnees**.


Ouvrez un nouveau projet QGIS, et à partir de l'explorateur, ajoutez la couche *ne_110m_admin_0_countries*. **Notez qu'il n'est pas nécessaire de dézipper le fichier pour visualiser les données dans QGIS !** Ceci est très pratique quand on est par exemple à la recherche de données sur internet et évite de dézipper tous les fichiers et donc de se retrouver avec beaucoup de dossiers. Il faudra cependant décompresser les données pour pouvoir les éditer.



[![visualisation dans QGIS de la couche ne_110m_admin_0_countries](illustrations/3_1_donnees_naturalearth.jpg)](illustrations/3_1_donnees_naturalearth.jpg "illustrations/3_1_donnees_naturalearth.jpg")


#### Avec les données SRTM


Nous avons vu jusqu'ici le téléchargement de quelques données vecteur. Les données raster seront par exemple des images satellite, des fonds de carte, des [modèles numériques de terrain (MNT)](http://fr.wikipedia.org/wiki/Mod%C3%A8le_num%C3%A9rique_de_terrain "http://fr.wikipedia.org/wiki/Mod%C3%A8le_num%C3%A9rique_de_terrain")...


Nous allons ici télécharger un **modèle d'élévation pour le Kenya**.


Un **modèle d'élévation numérique (Digital Elevation Model ou DEM)** se rapproche d'un MNT, mais il ne mesure pas l'altitude au sol mais l'altitude des éléments présents au sol. Si une forêt est présente, ce sera donc l'altitude du sommet des arbres qui sera mesurée et non l'altitude du sol, idem si des bâtiments sont présents.


On trouve sur internet deux DEM à couverture mondiale en libre accès : le modèle **ASTER** issu d'une collaboration NASA/METI (Ministry of Economy, Trade and Industry of Japan) et le modèle **SRTM** issu d'une collaboration NASA/NGA (National Geospatial-Intelligence Agency). Nous allons voir ici le cas du SRTM.



Rendez-vous sur [http://dwtkns.com/srtm/](http://dwtkns.com/srtm/ "http://dwtkns.com/srtm/"). Un avertissement en haut de la page indique que l'outil ne fonctionne plus, mais il semble néanmoins opérationnel.


Cliquez sur une des cases recouvrant le Kenya (par exemple la dalle **srtm_44_12**) :



[![téléchargement d'une dalle du SRTM](illustrations/3_1_telechargement_srtm.jpg)](illustrations/3_1_telechargement_srtm.jpg "illustrations/3_1_telechargement_srtm.jpg")

Téléchargez la dalle au format GeoTIFF, placez le fichier dans votre dossier **TutoQGIS_03_RechercheDonnees/donnees**. Il n'est pas nécessaire de dézipper le fichier obtenu.


Dans QGIS, ajoutez le fichier TIF téléchargé au moyen de l'explorateur.



[![superposition des cours d'eau, des régions et du SRTM](illustrations/3_1_srtm_kenya.jpg)](illustrations/3_1_srtm_kenya.jpg "illustrations/3_1_srtm_kenya.jpg")

Au cas où le téléchargement échouerait, cette couche est également disponible [avec les autres données du tutoriel](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip").



### Et tout le reste ?


Selon la zone sur laquelle vous travaillez et votre sujet, il existe de nombreux sites avec des données géographiques en téléchargement. En voici quelques uns en vrac, qui seront ou non pertinents pour vous :


* Natural Earth : données à l'échelle mondiale : limites administratives, hydrographie, bathymétrie, fonds de carte raster...


[http://www.naturalearthdata.com/downloads/](http://www.naturalearthdata.com/downloads/ "http://www.naturalearthdata.com/downloads/")
* FAO (Food and Agriculture Organisation) : catalogue de métadonnées donnant accès à un large éventail de données vecteur ou raster, en particulier sur les pays du Sud.


[http://www.fao.org/geonetwork/](http://www.fao.org/geonetwork/ "http://www.fao.org/geonetwork/")
* geo.data.gouv.fr : portail national français de données géographiques


[https://geo.data.gouv.fr/fr/](https://geo.data.gouv.fr/fr/ "https://geo.data.gouv.fr/fr/")
* OpenStreetMap : extractions de données au format SHP ou OSM, fourni par Geofabrik :


[http://download.geofabrik.de/](http://download.geofabrik.de/ "http://download.geofabrik.de/")
* IGN : nombreuses données disponibles pour la France, dont un grand nombre en libre accès


[https://geoservices.ign.fr/catalogue](https://geoservices.ign.fr/catalogue "https://geoservices.ign.fr/catalogue")
* cadastre.data.gouv.fr : données cadastrales françaises en opendata


[https://cadastre.data.gouv.fr/datasets/plan-cadastral-informatise](https://cadastre.data.gouv.fr/datasets/plan-cadastral-informatise "https://cadastre.data.gouv.fr/datasets/plan-cadastral-informatise")
 (pour exploiter les données du cadastre au format edigeo sous QGIS : voir [ce projet](http://atelier.adullact.org/projects/edigeo/ "http://atelier.adullact.org/projects/edigeo/") et [sa documentation](http://atelier.adullact.org/frs/download.php/file/8387/documentationEDIGEO-0.90.pdf "http://atelier.adullact.org/frs/download.php/file/8387/documentationEDIGEO-0.90.pdf"))
* THEIA : structure nationale inter-organismes ayant pour vocation de faciliter l’usage des images satellite


[http://www.theia-land.fr/](http://www.theia-land.fr/ "http://www.theia-land.fr/")
* GADM : limites administratives accessibles par pays


[http://www.gadm.org/](http://www.gadm.org/ "http://www.gadm.org/")
* DIVA-GIS : site du logiciel SIG libre DIVA, où sont aussi disponibles des données vecteur sur les limites administratives, l'hydrographie, le transport, la population... classées par pays


[http://www.diva-gis.org/gdata](http://www.diva-gis.org/gdata "http://www.diva-gis.org/gdata")
* ASTER : modèle d'élévation, données mondiales téléchargeables par dalles


[https://search.earthdata.nasa.gov/](https://search.earthdata.nasa.gov/ "https://search.earthdata.nasa.gov/")
* SRTM : modèle d'élévation, données mondiales téléchargeables par dalles


[http://dwtkns.com/srtm/](http://dwtkns.com/srtm/ "http://dwtkns.com/srtm/")


Vous pouvez également tester une recherche internet avec quelques mots clés, de préférence dans la langue du pays ou en anglais, ainsi que par exemple le mot clé *shapefile*, qui reste un format de données SIG très utilisé. De manière générale, on trouve beaucoup de données accessibles en téléchargement, mais attention à la date de ces données, à leur échelle, leur mode de fabrication... qui peuvent ne pas être en adéquation avec vos questions.




[chapitre précédent](03_00_recherche_ajout.php "03_00_recherche_ajout.php")
[chapitre suivant](03_02_donnees_flux.php "03_02_donnees_flux.php")


[haut de page](#wrap "#wrap")
