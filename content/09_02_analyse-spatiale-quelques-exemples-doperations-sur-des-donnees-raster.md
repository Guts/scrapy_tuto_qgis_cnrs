
## IX.2 Analyse spatiale : quelques exemples d'opérations sur des données raster


* [Préparation des données : découpage d'un raster](#IX21 "#IX21")
* [Explorer les données en modifiant le mode de représentation](#IX22 "#IX22")
	+ [Répartition des valeurs : histogramme de fréquence](#IX22a "#IX22a")
	+ [La valeur des pixels sans valeur](#IX22b "#IX22b")
	+ [Modifier le style pour explorer les données](#IX22c "#IX22c")
* [Manipuler les données : extraction de valeurs](#IX23 "#IX23")
* [Exemples d'opérations sur des données d'altitude](#IX24 "#IX24")
	+ [Création de courbes de niveau](#IX24a "#IX24a")
	+ [Projection d'un raster](#IX24b "#IX24b")
	+ [Calcul de pente à partir du raster projeté](#IX24c "#IX24c")




Vous verrez ici quelques manipulations sur un raster d'altitude, appliquées au [modèle d'élévation numérique (MNE)](03_01_donnees_internet.php#III12b "03_01_donnees_internet.php#III12b") de la Jamaïque.


### Préparation des données : découpage d'un raster


Le but sera ici de découper un raster pour ne garder que la zone qui nous intéresse. Cette manipulation permet d'alléger les données et les futurs traitements.



Ouvrez un nouveau projet QGIS. [Ajoutez la couche raster](01_02_info_geo.php#I24 "01_02_info_geo.php#I24") *[srtm_21_09.tif](donnees/TutoQGIS_09_AnalyseSpat.zip "donnees/TutoQGIS_09_AnalyseSpat.zip")* située dans **TutoQGIS_09_AnalyseSpat/donnees**.


Le but va être de ne garder que la partie du MNE correspondant à la Jamaïque, en éliminant les parties de Cuba et des îles Caïman.



[![MNE sur fond OSM, la partie à garder est encadrée en rouge](illustrations/9_2_decoupage_principe.jpg)](illustrations/9_2_decoupage_principe.jpg "illustrations/9_2_decoupage_principe.jpg")
MNE sur fond OpenStreetMap. En gris transparent, l'emprise de la couche, en rouge encadré, la partie à conserver.

Rendez-vous dans la
 [boîte à outils → GDAL → Extraction raster → Découper un raster selon une emprise

![Menu Raster, Extraction, Découper](illustrations/9_2_raster_decouper_menu.jpg)](#thumb "#thumb")
 :



[![Emplacement de l'outil de découpe dans la boîte à outils](illustrations/9_2_raster_decouper_fenetre.jpg)](illustrations/9_2_raster_decouper_fenetre.jpg "illustrations/9_2_raster_decouper_fenetre.jpg")

* Couche source : sélectionnez *srtm_21_09*
* Etendue de découpage : cliquez sur le bouton **...** tout à droite, choisissez **Dessiner sur le canevas**. Il faut ensuite dessiner l'emprise à garder, toujours dans l'outil de découpage. Dessinez un rectangle approximatif autour de l'île de la Jamaïque :
 [![Menu Raster, Extraction, Découper](illustrations/9_2_decoupe_jam.jpg)](illustrations/9_2_decoupe_jam.jpg "illustrations/9_2_decoupe_jam.jpg")
* Découpé (étendue) : cliquez sur le bouton à droite **...** et choisissez où la nouvelle couche sera créée, et son nom : *srtm_jamaique*
* Cliquez ensuite sur **Exécuter**.


Une fois l'opération terminée, fermez la fenêtre de l'outil de découpage.


Dans la liste des couches, décochez srtm_21_09 pour ne voir que la couche découpée : elle ne comprend que la Jamaïque.



[![srtm avant découpage](illustrations/9_2_decoupage_avant.jpg)](illustrations/9_2_decoupage_avant.jpg "illustrations/9_2_decoupage_avant.jpg")
[![srtm après découpage](illustrations/9_2_decoupage_apres.jpg)](illustrations/9_2_decoupage_apres.jpg "illustrations/9_2_decoupage_apres.jpg")
SRTM avant et après découpage.


Notez qu'il est également possible de découper un raster suivant l'emprise d'une couche de polygones, en utilisant l'option **Utiliser l'emprise de la couche**. Vous pouvez aussi directement rentrer à la main les coordonnées de l'emprise à conserver.


### Explorer les données en modifiant le mode de représentation


Les données ne contiennent maintenant plus que la zone d'étude et sont donc prêtes pour la suite... Mais au fait, que contiennent-elles, ces données ?


Avant de créer de nouvelles données à partir de ce MNE, ou bien de le croiser avec d'autres couches, il peut être judicieux d'explorer un peu ces données. Pour cela, il est possible de faire beaucoup de choses en allant simplement dans les propriétés de la couche  !


#### Répartition des valeurs : histogramme de fréquence


Une manière simple d'avoir un aperçu du contenu des données est de visualiser l'histogramme de fréquence des valeurs des pixels. Vous pourrez ainsi voir d'un coup d'œil la répartition des valeurs d'élévation.



**Propriétés de la couche *srtm_jamaique* → rubrique Histogramme** : cliquez sur le bouton **Calculer l'histogramme**.



[![Rubrique histogramme des propriétés de la couche](illustrations/9_2_histogramme.jpg)](illustrations/9_2_histogramme.jpg "illustrations/9_2_histogramme.jpg")


L'axe horizontal représente les valeurs de pixels, donc ici d'élévation. L'axe vertical représente le nombre de pixels ayant une valeur donnée. Il est également possible de lire les valeurs minimale et maximale sou l'histogramme.


On peut voir d'un seul coup d'œil que beaucoup de pixels ont une valeur inférieure à 100 mètres d'élévation.



Il est possible de zoomer sur le graphique en dessinant un rectangle, ou bien en modifiant les valeurs min et max. Un clic droit permet de revenir à la vue initiale.



#### La valeur des pixels sans valeur


Une information utile à savoir est la **valeur des pixels « sans données »**. En effet, vous ne voyez dans QGIS que les pixels de la Jamaïque et non ceux de l'océan les environnant, bien que nous ayons précédemment découpé cette couche suivant un rectangle.


En fait, **un raster étant un tableau, son emprise sera toujours rectangulaire et tous les pixels auront toujours une valeur**. Cependant, par commodité, on donne une valeur aberrante aux pixels « sans données ». D'où ce titre énigmatique !



Pour savoir quelle est cette valeur : **propriétés de la couche → rubrique Transparence** :



[![Rubrique Transparence des propriétés de la couche, avec encadré la valeur nulle des pixels](illustrations/9_2_nodata.jpg)](illustrations/9_2_nodata.jpg "illustrations/9_2_nodata.jpg")

Regardez la valeur à droite de **Aucune valeur de données** : pour cette couche, cette valeur est de **-32768**.



Il est évident que l'élévation n'est jamais de -32768 mètres : il s'agit d'une valeur aberrante pour indiquer que certains pixels n'ont pas de valeur d'élévation associée.


**Le logiciel gère cela en rendant ces pixels transparents par défaut.**



Pour tester cela, décochez la case devant **Aucune valeur de données** et fermez la fenêtre des propriétés. Vous pouvez voir toute l'emprise de la couche, y compris les pixels sans données.


![icône identifier les entités](illustrations/1_2_informations_icone.jpg)Vous pouvez utiliser l'outil **Identifier des entités** pour cliquer sur un pixel « sans données » sur le bord du raster et voir que sa valeur correspond bien à -32768.



[![SRTM Jamaïque en visualisant toutes les valeurs, y compris la valeur -32768](illustrations/9_2_test_nodata.jpg)](illustrations/9_2_test_nodata.jpg "illustrations/9_2_test_nodata.jpg")

Retournez dans les propriétés de la couche et recochez la case **Aucune valeur de données**.


Si vous utilisez à nouveau l'outil d'identification sur un pixel du bord du raster (désormais invisible), vous verrez qu'il est maintenant considéré comme « sans données ». En cliquant en-dehors de l'emprise du raster, l'outil d'identification ne renvoie aucun résultat.



Pourquoi la valeur -32768 ? Voici quelques explications si vous désirez en savoir plus. Il existe différents types de raster : 8 bits, 16 bits, 32 bits... Ce qui correspond en fait au nombre de bits sur lesquels est stockée la valeur d'un pixel.


Ici, notre raster est de type 16 bits (ce que vous pouvez vérifier en allant dans les propriétés de la couche, rubrique Information). Chaque valeur de pixel est codée sur 16 bits, ce qui donne 216 soit 65536 possibilités. Les valeurs pouvant être positives ou négatives, elles vont de -32768 à 32767, puisque 65536/2=32768.


La valeur nulle est donc la valeur la plus aberrante possible, ici -32768.


Rendez-vous [ici](http://desktop.arcgis.com/fr/arcmap/10.3/manage-data/raster-and-images/bit-depth-capacity-for-raster-dataset-cells.htm "http://desktop.arcgis.com/fr/arcmap/10.3/manage-data/raster-and-images/bit-depth-capacity-for-raster-dataset-cells.htm") pour en savoir plus sur les différents types de raster et les données qu'ils peuvent contenir. En règle général, on choisit le type codé sur le moins de bits possibles en restant compatible avec les données, pour obtenir des rasters moins lourds.


#### Modifier le style pour explorer les données


Une manière simple d'explorer les données, aussi bien pour un vecteur que pour un raster, est de modifier la manière dont sont représentées les données.



Rendez-vous dans les propriétés de la couche, rubrique **Symbologie**.


A la place de **Bande grise unique**, sélectionnez **Pseudo-couleur à bande unique** et appliquez les changements (sans forcément fermer la fenêtre des propriétés).



[![Fenêtre des propriétés, Symbologie, style pseudo-couleur à bande unique](illustrations/9_2_style_pseudocouleur.jpg)](illustrations/9_2_style_pseudocouleur.jpg "illustrations/9_2_style_pseudocouleur.jpg")


[![Fenêtre des propriétés, Symbologie, style pseudo-couleur à bande unique](illustrations/9_2_style_pseudocouleur_res.jpg)](illustrations/9_2_style_pseudocouleur_res.jpg "illustrations/9_2_style_pseudocouleur_res.jpg")

Ce style permet de choisir le degradé de couleur utilisé pour étirer les valeurs.


Choisissez maintenant un mode d'interpolation **discret** au lieu de linéaire.


[![Choix du mode d'interpolation discret dans les propriétés, rubrique Style](illustrations/9_2_interpol_discret.jpg)](illustrations/9_2_interpol_discret.jpg "illustrations/9_2_interpol_discret.jpg")
Appliquez les changements :



[![Elevations en classes du orange clair au marron (mode discret)](illustrations/9_2_style_discret.jpg)](illustrations/9_2_style_discret.jpg "illustrations/9_2_style_discret.jpg")

**Les valeurs sont maintenant représentées par classes.**


Il est possible de modifier les classes, soit de manière automatique en choisissant le mode **intervalle égal** ou **quantile** et le nombre de classes, sous le tableau des valeurs, soit à la main en double-cliquant sur une valeur dans le tableau.


Pour en savoir plus sur les méthodes de discrétisation : voir notamment [ici](https://blog.m0le.net/2014/09/08/cartographie-numerique-precis-de-discretisation-pour-les-nuls/ "https://blog.m0le.net/2014/09/08/cartographie-numerique-precis-de-discretisation-pour-les-nuls/").


Par exemple, modifiez les classes pour faire apparaître les pixels de valeur inférieure à 100 mètres, comprise entre 100 et 700 mètres et supérieure à 700 mètres :



[![Fenêtre Symbologie : 3 classes, valeurs seuil 100, 700 et max](illustrations/9_2_style_discret_3classes.jpg)](illustrations/9_2_style_discret_3classes.jpg "illustrations/9_2_style_discret_3classes.jpg")


[![3 classes, valeurs seuil 100, 700 et max : visualisation](illustrations/9_2_style_discret_3classes_res.jpg)](illustrations/9_2_style_discret_3classes_res.jpg "illustrations/9_2_style_discret_3classes_res.jpg")


En modifiant le style des données, notamment en discrétisant les données et en faisant varier les classes, on peut avoir une meilleure idée du sujet étudié, ici l'élévation de la Jamaïque. C'est une première approche !


### Manipuler les données : extraction de valeurs


Admettons maintenant que l'étape précédente nous ait permis de décider qu'on souhaite s'intéresser uniquement à la zone inférieure à 100 mètres d'altitude.


**Comment faire pour obtenir un nouveau raster, où les pixels d'élévation inférieure à 100 mètres ont une valeur de 1 et les autres une valeur de 0 ?** Une telle couche pourra servir par exemple de masque, ou bien pour ne garder que les valeurs d'un raster portant sur un autre thème de la zone inférieure à 100 mètres.



Rendez-vous dans la
 [boîte à outils → Analyse raster → Raster calculator

![Menu Raster, Analyse raster, Calculatrice raster](illustrations/9_2_rastercalc_menu.jpg)](#thumb "#thumb")
 :



[![Fenêtre de la calculatrice raster, avec la formule "srtm_jamaique@1" < 100](illustrations/9_2_rastercalc_fenetre.jpg)](illustrations/9_2_rastercalc_fenetre.jpg "illustrations/9_2_rastercalc_fenetre.jpg")


Cet outil permet d'effectuer des calculs sur des rasters, par exemple soustraire un raster à un autre. Nous l'utiliserons ici pour obtenir un raster où les pixels d'élévation inférieure à 100 mètres ont une valeur de 1 et les autres une valeur de 0.



* Dans la partie **Couches** en haut à gauche, double-cliquez sur *srtm_jamaique* pour faire apparaître le nom de la couche dans la partie **Expression** en-dessous
* Complétez l'expression en rajoutant à la main **< 100** : l'expression complète est donc **"srtm_jamaique@1" < 100**
* Dans la partie **Reference Layer(s)**, cliquez sur le bouton **...** à doite et sélectionnez la couche *srtm_jamaique*, pour que le raster créé ait la même emprise, résolution et CRS


Exécutez... Le nouveau raster (temporaire) est ajouté.



Comment l'expression **"srtm_jamaique@1" < 100** nous pemet-elle d'obtenir le résultat souhaité ? Cette expression est évaluée pour chaque pixel, le résultat est soit vrai (1) soit faux (0).



Contrairement à ce à quoi on aurait pu s'attendre, on peut voir en noir les valeurs supérieure à 100 mètres. Cependant, en interrogeant le raster avec l'outil d'identification on peut voir que les pixels qui avaient une élévation < 100 mètres ont maintenant une valeur de 1, et les autres 0.


Il est facile de changer le mode de représentation, par exemple dans les **propriétés → Symbologie → Dégradé de couleur** : choisir **Blanc vers noir** au lieu de Noir vers blanc.



[![propriétés rubrique symbologie : blanc vers noir](illustrations/9_2_blancversnoir.jpg)](illustrations/9_2_blancversnoir.jpg "illustrations/9_2_blancversnoir.jpg")


[![propriétés rubrique symbologie : blanc vers noir](illustrations/9_2_blancversnoir_res.jpg)](illustrations/9_2_blancversnoir_res.jpg "illustrations/9_2_blancversnoir_res.jpg")


Cette couche pourra servir par exemple de masque, telle quelle ou bien en la transformant en couche vecteur au moyen de l'outil Polygoniser.


### Exemples d'opérations sur des données d'altitude


Il existe un certain nombre d'opérations proposées par les logiciels SIG sur les rasters d'altitude, par exemple la création de courbes de niveaux, d'ombrage, de pente... Nous verrons ici 2 exemples, sur les courbes de niveau et le calcul de pente.


#### Création de courbes de niveau


Les courbes de niveaux sont des lignes imaginaires joignant tous les points situés à la même altitude. Nous allons créer des courbes de niveau distantes de 100 mètres à partir du MNE de la Jamaïque.



[![extrait de carte avec courbes de niveaux](illustrations/9_2_isohypses_exemple.jpg)](illustrations/9_2_isohypses_exemple.jpg "illustrations/9_2_isohypses_exemple.jpg")
Un extrait de carte avec des courbes de niveau (Source : [Wikimedia](https://commons.wikimedia.org/wiki/File:Cntr-map-1.jpg "https://commons.wikimedia.org/wiki/File:Cntr-map-1.jpg"))


Rendez-vous dans la
 [boîte à outils → GDAL → Extraction raster → Courbe de niveau

![Emplacement de l'outil Contour dans la boîte à outils](illustrations/9_2_contours_menu.jpg)](#thumb "#thumb")
 (dans les versions pécédentes de QGIS, cet outil peut se nommer *contour*) :



[![Fenêtre de l'outil de création de contours](illustrations/9_2_contours_fenetre.jpg)](illustrations/9_2_contours_fenetre.jpg "illustrations/9_2_contours_fenetre.jpg")

* Couche source : sélectionnez *srtm_jamaique*
* Intervalle entre les courbes de niveaux : tapez **100** pour un intervalle de 100 mètres
* **Nom de l'attribut :** il s'agit du nom du champ qui contiendra l'altitude de la courbe. Vous pouvez laisser la valeur par défaut **ELEV**, ou bien taper le nom de votre choix


Cliquez sur **Exécuter** :



[![Visualisation des courbes de niveau](illustrations/9_2_courbes_carte.jpg)](illustrations/9_2_courbes_carte.jpg "illustrations/9_2_courbes_carte.jpg")
[![Visualisation des courbes de niveau](illustrations/9_2_courbes_table.jpg)](illustrations/9_2_courbes_table.jpg "illustrations/9_2_courbes_table.jpg")


Une couche de lignes a été créée. Chaque ligne possède en attribut son élévation, qui varie ici de 0 à 2200 mètres.


#### Projection d'un raster


Il est également possible de créer à partir d'un raster d'altitude un raster de pente : chaque pixel aura la valeur de la pente en ce point. Pour en savoir plus sur la manière dont est calculée la pente, vous pouvez vous référer à [l'aide d'ArcGIS](http://resources.arcgis.com/fr/help/main/10.1/index.html#//00q90000001r000000 "http://resources.arcgis.com/fr/help/main/10.1/index.html#//00q90000001r000000") sur ce point.


[![Représentation de la pente](illustrations/9_2_pente.jpg)](illustrations/9_2_pente.svg "illustrations/9_2_pente.svg")
La pente est calculée en fonction de la distance horizontale et de la hauteur. Dans notre cas, la hauteur est en mètres, et la distance horizontale en degrés. Les deux unités étant différentes, le calcul de pente donnera des valeurs aberrantes.


La première étape est donc de **projeter notre raster, pour obtenir des unités identiques verticalement et horizontalement.**


Quelle projection utiliser pour notre raster ?


En règle générale, il y a deux possibilités quand on cherche une projection pour un pays : utiliser une projection nationale, ou bien une [projection UTM](02_02_coord.php#II22d "02_02_coord.php#II22d").


Pour savoir s'il existe dans QGIS des projections nationales pour la Jamaïque, vous pouvez faire une recherche dans les SCR proposés.



![icône SCR](illustrations/2_3_scr_projet_icone.jpg)Rendez-vous dans les propriétés du projet, rubrique SCR, par exemple en cliquant sur l'icône de sphère tout en bas à droite de la fenêtre de QGIS :



[![Recherche d'un SCR pour la Jamaïque](illustrations/9_2_scr_jamaica.jpg)](illustrations/9_2_scr_jamaica.jpg "illustrations/9_2_scr_jamaica.jpg")

Tapez **jamaica** dans la rubrique **Filtre** : plusieurs réponses sont proposées, dont 3 SCR projetés. Une rapide recherche internet semble indiquer que le SCR **JAD2001** est le plus récent (source : [http://www.jamaicancaves.org/jad2001.htm](http://www.jamaicancaves.org/jad2001.htm "http://www.jamaicancaves.org/jad2001.htm")). C'est donc ce SCR que nous utiliserons.


Sélectionnez **JAD2001 (code EPSG:3448) et cliquez sur **OK**.**



Nous venons de changer le SCR du projet, mais pas celui de notre raster (pour rappel, voir [ici](02_03_couches_projets.php "02_03_couches_projets.php")).



Une étape préliminaire avant de projeter le raster : ouvrez les propriétés du raster, rubrique **Information**, sous-rubrique **Bandes**, recherchez **Aucune valeur de données**. Vous devriez avoir -32768, notez cette valeur. C'est celle utilisée pour les pixels « sans valeur » (qui ont donc en réalité la valeur -32768), en-dehors de l'île.


Ensuite, pour changer le SCR du raster :
 [Boîte à outils → GDAL → Projections raster → Projection (warp)

![Menu Raster , Projections, Projection...](illustrations/9_2_reproj_raster_menu.jpg)](#thumb "#thumb")
 :



[![Fenêtre de reprojection du raster](illustrations/9_2_reproj_raster_fenetre.jpg)](illustrations/9_2_reproj_raster_fenetre.jpg "illustrations/9_2_reproj_raster_fenetre.jpg")

* Couche source : sélectionnez *srtm_jamaique* dans la liste
* SCR cible : cliquez sur le bouton à droite pour rechercher le SCR **JAD2001 code EPSG:3448**
* Valeur Nodata : tapez la [valeur des pixels sans données](09_02_raster.php#IX22b "09_02_raster.php#IX22b") : **-32768**
* Laissez tous les autres paramètres par défaut, cliquez sur **Exécuter**.


Patientez... La nouvelle couche est ajoutée, vous pouvez vérifier dans ses propriétés (rubrique Source) que son SCR soit bien le JAD2001.



[![scr de la nouvelle couche : JAD2001](illustrations/9_2_scr_ok.jpg)](illustrations/9_2_scr_ok.jpg "illustrations/9_2_scr_ok.jpg")

Il semblerait qu'il ne soit plus utile de préciser la valeur NoData, celle-ci étant automatiquement lue dans les propriétés du raster en entrée !


Supprimez les autres couches, pour ne garder dans le projet que la couche *srtm_jamaique_JAD2001*.



#### Calcul de pente à partir du raster projeté



Rendez-vous dans la
 [boîte à outils → GDAL → Analyse raster → Pente

![Menu Raster, Analyse, MNT/DEM (Modèles de terrain)](illustrations/9_2_pente_menu.jpg)](#thumb "#thumb")
 :



[![Fenêtre de calcul de pente](illustrations/9_2_pente_fenetre.jpg)](illustrations/9_2_pente_fenetre.jpg "illustrations/9_2_pente_fenetre.jpg")

* Couche source : sélectionnez *srtm_jamaique_JAD2001*
* Laissez les autres paramètres par défaut (pour plus d'infos sur les méthodes de Zevenberger & Thorne et Horn : [http://www.macaulay.ac.uk/LADSS/documents/DEMs-for-spatial-modelling.pdf](http://www.macaulay.ac.uk/LADSS/documents/DEMs-for-spatial-modelling.pdf "http://www.macaulay.ac.uk/LADSS/documents/DEMs-for-spatial-modelling.pdf"), pp. 12 et 13).


Cliquez sur **Exécuter**, patientez... la couche s'affiche :



[![la couche de pentes](illustrations/9_2_pente_res.jpg)](illustrations/9_2_pente_res.jpg "illustrations/9_2_pente_res.jpg")

Ici, les pixels sombres représentent des pentes faibles et les pixels clairs de fortes pentes.


![menu projet, sauvegarder sous...](illustrations/8_2_id_icone.jpg)En cliquant sur un pixel avec l'outil **Identifier les entités**, vous pouvez connaître la valeur de la pente pour ce pixel :



[![la couche de pentes](illustrations/9_2_id_pente.jpg)](illustrations/9_2_id_pente.jpg "illustrations/9_2_id_pente.jpg")

Ici, le pixel a une pente de 13,5° environ.



Il existe beaucoup d'autres traitements possibles sur les données raster. Mais pourquoi toujours opposer raster et vecteur ? Dans le prochain chapitre, découvrez comment les faire fonctionner main dans la main !




[chapitre suivant](09_03_vecteur_raster.php "09_03_vecteur_raster.php")
[chapitre précédent](09_01_vecteur.php "09_01_vecteur.php")


[haut de page](#wrap "#wrap")
