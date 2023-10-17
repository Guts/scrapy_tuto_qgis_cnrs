
## X.1 Représenter des données : différentes méthodes adaptées à différents cas


* [Représenter des quantités ou des effectifs : carte en symboles proportionnels](#X11 "#X11")
	+ [Créer une couche de points à partir d'une couche de polygones](#X11a "#X11a")
	+ [Faire varier la surface de points en fonction d'un champ](#X11b "#X11b")
	+ [Surface, rayon, Flannery... Pour en savoir plus sur les différentes méthodes](#X11c "#X11c")
	+ [Les plus petits devant ! Modifier l'ordre d'affichage des symboles](#X11d "#X11d")
	+ [C'est mieux avec la légende](#X11e "#X11e")
* [Représenter des variables relatives à des surfaces : cartes choroplèthes](#X12 "#X12")
	+ [Créer un champ de densité de population](#X12a "#X12a")
	+ [Faire varier la couleur des communes en fonction du champ densité](#X12b "#X12b")
* [Représenter des quantités ou des effectifs : cartes en semis de points](#X13 "#X13")
* [Connaître la distribution de ses données](#X14 "#X14")
	+ [Histogramme simple](#X14a "#X14a")
	+ [Histogramme avec l'extension Plotly](#X14b "#X14b")


Il existe de nombreuses manières de représenter les données. Nous en avons abordées certaines dans les précédentes parties, et nous en verrons quelques unes plus en détail ici. Il en existe beaucoup d'autres !


Le [chapitre suivant](10_02_mise_en_page.php "10_02_mise_en_page.php") abordera quant à lui la mise en page proprement dite, dans le module dédié de QGIS, qui permet d'exporter une carte avec légende, titre, échelle...


A partir d'une couche de communes et leur population, nous allons voir différentes manières de visualiser cette population.


**Nous ne parlerons pas ici, ou très peu, de sémiologie graphique et du choix du mode de représentation**, ce qui a déjà été fait dans de nombreux ouvrages, notamment :


* *Sémiologie graphique: Les diagrammes - Les réseaux - Les cartes* de Jacques Bertin
* *Manuel de cartographie* de Nicolas Lambert et Christine Zanin
* *Pratiques de la cartographie* d'Anne Le Fur


### Représenter des quantités ou des effectifs : carte en symboles proportionnels


Les cartes en symbole proportionnels permettent la représentation de quantités ou d'effectifs par des symboles, généralement des cercles. La surface des symboles sera proportionnelle à la quantité ou l'effectif.



[![Exemple d'une carte en cercles proportionnels sur les ouvriers et cadres en Occitanie](illustrations/10_01_exemple_cercleprop.jpg)](https://neocarto.hypotheses.org/5064 "https://neocarto.hypotheses.org/5064")
Exemple d'une carte en cercles proportionnels réalisée par Nicolas Lambert et Ronan Ysebaert (2018). Source : [carnet (néo)cartographique](https://neocarto.hypotheses.org/5064 "https://neocarto.hypotheses.org/5064").

#### Créer une couche de points à partir d'une couche de polygones


Dans QGIS, la visualisation de données sous forme de cercles proportionnels peut se faire directement à partir d'une couche de polygone (c'est alors les centroïdes des polygones qui sont représentés) mais est plus simple à partir d'une couche de points.


**A partir de la couche de communes, nous allons créer les centroïdes (barycentres) des communes.**


Qu'est-ce que le [centroïde](https://en.wikipedia.org/wiki/Centroid "https://en.wikipedia.org/wiki/Centroid") d'un polygone ? Il s'agit du centre géométrique de ce polygone. Concrètement, cela correspond au point où une forme en papier du polygone tiendrait en équilibre sur une épingle. Sans entrer dans le détail du calcul des coordonnées d'un centroïde, l'idée est de minimiser la distance au carré de ce centroïde à chacun des sommets du polygone.



[![Communes et leur centroïde](illustrations/10_01_centroides_principe.jpg)](illustrations/10_01_centroides_principe.jpg "illustrations/10_01_centroides_principe.jpg")
Exemple de polygones (en gris) et de leurs centroïdes (en rouge).

**Les centroïdes peuvent se situer en-dehors des polygones**, comme par exemple dans le cas de la commune de Remoiville dans la Meuse :



[![Exemple d'un polygone biscornu et de son centroïde qui tombe en-dehors](illustrations/10_01_centroides_dehors.jpg)](illustrations/10_01_centroides_dehors.jpg "illustrations/10_01_centroides_dehors.jpg")

Dans notre utilisation, cela nous est égal que le centroïde soit au centre exact du polygone ; par contre, **il sera plus lisible qu'il tombe toujours à l'intérieur du polygone**. Il existe donc généralement dans les logiciels SIG une variante de l'outil de centroïdes, qui crée des centroïdes parfois imparfaits mais toujours dans les polygones !


C'est la raison pour laquelle nous allons utiliser ici l'outil **Point dans la surface** plutôt que l'outil **Centroïdes**.



Ouvrez un nouveau projet QGIS, ajoutez la couche *[COMMUNE.shp](donnees/TutoQGIS_10_Representation.zip "donnees/TutoQGIS_10_Representation.zip")* située dans le dossier **TutoQGIS_10_representation/donnees**.


Dans la barre de recherche de la boîte à outils, tapez par exemple *point dans* pour trouver plus facilement l'outil **point dans la surface** (rubrique Géométrie vectorielle) :



[![Emplacement de l'outil 'point dans la surface' dans la toolbox](illustrations/10_01_centroides_menu.jpg)](illustrations/10_01_centroides_menu.jpg "illustrations/10_01_centroides_menu.jpg")

Double-cliquez sur cet outil :



[![Fenêtre de l'outil centroïdes](illustrations/10_01_centroides_fenetre.jpg)](illustrations/10_01_centroides_fenetre.jpg "illustrations/10_01_centroides_fenetre.jpg")

* Couche source : choisir la couche *COMMUNE*
* Point cliquez sur le bouton à droite **...**, allez à l'emplacement où vous voulez créer la couche de centroïdes et donnez-lui un nom : *communes_centroides*


**Exécuter**... La couche de centroïdes est ajoutée à QGIS : un point a été créé par commune.



[![Visualisation des centroïdes sur la carte](illustrations/10_01_centroides_visu.jpg)](illustrations/10_01_centroides_visu.jpg "illustrations/10_01_centroides_visu.jpg")


#### Faire varier la surface de points en fonction d'un champ


Il est ensuite possible de faire varier la surface des centroïdes des communes en fonction d'un champ, ou d'une expression :



Couche *communes_centroides* : **Propriétés → Symbologie → bouton à droite de Taille → Assistant...** :



[![Accès à l'Assistant Taille dans la rubrique style des propriétés de la couche](illustrations/10_01_assistant_taille_acces.jpg)](illustrations/10_01_assistant_taille_acces.jpg "illustrations/10_01_assistant_taille_acces.jpg")


[![Fenêtre de l'Assistant Taille](illustrations/10_01_assistant_fenetre.jpg)](illustrations/10_01_assistant_fenetre.jpg "illustrations/10_01_assistant_fenetre.jpg")


Le principe est simple : cet outil lit les valeurs minimum et maximum pour un champ de la table attributaire, et leur fait correspondre une surface minimum et maximum. Les surfaces correspondant aux valeurs intermédiaires sont interpolées.



**Partie Saisie** : cette partie concerne les valeurs de la variable utilisée.


* Source : il s'agit du champ dont les valeurs seront utilisées, ici **POPULATION**
* Valeurs depuis... à ... : cliquez sur le bouton Actualiser à droite pour lire automatiquement les valeurs minimum et maximum de population, ici 0 et 2190327


**Partie Sortie** : cette partie concerne la manière dont les valeurs seront représentées.


* Taille depuis... à ... : choisissez ici les surfaces correspondant aux valeurs minimale et maximale. Vous pouvez tester différentes valeurs, le résultat dépendra de l'échelle à laquelle la carte sera lue (France entière, département...)
* Méthode de calcul : choisissez **Surface** pour faire varier la surface et non le diamètre des cercles



#### Surface, rayon, Flannery... Pour en savoir plus sur les différentes méthodes


Pourquoi faire varier la surface des cercles et non leur rayon ? Tout simplement parce qu'ainsi les variations de forme vues par l'œil seront proportionnelles aux variations de la variable représentée. En faisant varier le rayon, l'œil verra un écart plus grand entre une valeur moyenne et une valeur élevée qu'entre une valeur faible et une valeur moyenne, même si la différence est la même.


La méthode de [Flannery](http://wiki.gis.com/wiki/index.php/Proportional_symbol_map#Apparent_Magnitude_.28Flannery.29_Scaling "http://wiki.gis.com/wiki/index.php/Proportional_symbol_map#Apparent_Magnitude_.28Flannery.29_Scaling") est une technique utilisée pour compenser le fait que, même si l'œil lit mieux les variations de surface que de taille, il ne les interprète cependant pas toujours exactement. Même si cette méthode est intéressante, étant donné que la méthode la plus utilisée en cartographie est de faire varier la surface, il n'est pas forcément recommandé de l'utiliser, à moins de bien le préciser sur votre carte.


La méthode exponentielle permet de surreprésenter les valeurs extrêmes (en ajustant l'exposant) et peut être utile à des fins d'exploration.



[![Légende cercles proportionnels avec la méthode Flannery (valeurs 1000, 100000, 1000000 et 2190327](illustrations/10_01_methode_flannery.jpg)](illustrations/10_01_methode_flannery.jpg "illustrations/10_01_methode_flannery.jpg")
[![Légende cercles proportionnels avec la méthode surface (valeurs 1000, 100000, 1000000 et 2190327](illustrations/10_01_methode_surface.jpg)](illustrations/10_01_methode_surface.jpg "illustrations/10_01_methode_surface.jpg")
[![Légende cercles proportionnels avec la méthode rayon (valeurs 1000, 100000, 1000000 et 2190327](illustrations/10_01_methode_rayon.jpg)](illustrations/10_01_methode_rayon.jpg "illustrations/10_01_methode_rayon.jpg")
[![Légende cercles proportionnels avec la méthode exponentiel (valeurs 1000, 100000, 1000000 et 2190327](illustrations/10_01_methode_exponentiel.jpg)](illustrations/10_01_methode_exponentiel.jpg "illustrations/10_01_methode_exponentiel.jpg")

Si vous ne devez retenir qu'une chose : **faites varier la surface de vos cercles, pas leur rayon !** Cela permettra une lecture plus juste du phénomène que vous représentez.


#### Les plus petits devant ! Modifier l'ordre d'affichage des symboles


Comme vous l'avez peut-être remarqué, QGIS affiche les cercles dans l'ordre de la table ; il peut donc arriver que de petits cercles soient masqués par de plus gros cercles.


Nous allons voir ici comment afficher les cercles par ordre de population, les plus faibles populations par-dessus.



[![Cercles dessinés dans l'ordre de la table](illustrations/10_01_ordre_avant.jpg)](illustrations/10_01_ordre_avant.jpg "illustrations/10_01_ordre_avant.jpg")
[![Cercles dessinés du plus peuplé au moins peuplé](illustrations/10_01_ordre_apres.jpg)](illustrations/10_01_ordre_apres.jpg "illustrations/10_01_ordre_apres.jpg")
A gauche, cercles dessinés dans l'ordre de la table ; à droite, cercles dessinés du plus grand au plus petit.


Dans les propriétés de la couche *communes_centroides*, **Symbologie**, tout en bas de la fenêtre, cliquez sur **Rendu de couche** :



[![Activer l'ordre de rendu des entités](illustrations/10_01_ordre_entites.jpg)](illustrations/10_01_ordre_entites.jpg "illustrations/10_01_ordre_entites.jpg")

Cochez la case **Contrôle de l'ordre de rendu des entités** et cliquez sur le bouton tout à droite :



[![Fenêtre de définition de l'ordre de rendu des entités](illustrations/10_01_ordre_entites_2.jpg)](illustrations/10_01_ordre_entites_2.jpg "illustrations/10_01_ordre_entites_2.jpg")

Choisissez le champ **POPULATION** et l'ordre **Descendant** : ainsi, les cercles seront dessinés du plus peuplé au moins peuplé.




[![Une partie de la carte en cercles proportionnels](illustrations/10_01_prop_visu.jpg)](illustrations/10_01_prop_visu.jpg "illustrations/10_01_prop_visu.jpg")

#### C'est mieux avec la légende


QGIS gère normalement les légendes pour les différents types de représentation, mais les cartes en cercles proportionnels présentent un cas particulier où nous devrons nous-même créer la légende.


Cette fonctionnalité a été rajoutée récemment, ce qui illustre bien le fait que les logiciels SIG ne sont pas initialement pensés comme des logiciels de cartographie (mais ils ont aujourd'hui tellement de possibilité en ce sens que ce serait dommage de se priver !).



Ouvrez la fenêtre des propriétés, rubrique **Symbologie**, et cliquez en bas à droite sur **Avancé** pour choisir **Légende pour la Taille définie par des données** :



[![Fenêtre des propriétés, symbologie, clic sur le bouton avancé](illustrations/10_01_legende_symbolprop_acces.jpg)](illustrations/10_01_legende_symbolprop_acces.jpg "illustrations/10_01_legende_symbolprop_acces.jpg")

Sous cet intitulé un peu obscur se cache une légende paramétrable pour notre carte en cercles proportionnels :



[![Fenêtre de la légende des symbols proportionnels](illustrations/10_01_legende_symbolprop.jpg)](illustrations/10_01_legende_symbolprop.jpg "illustrations/10_01_legende_symbolprop.jpg")

Dans la partie gauche, on peut spécifier les différents paramètres, un aperçu est mis à jour automatiquement dans la partie droite.


* Par défaut, la légende n'est pas activée. Nous allons choisir ici le mode **Légende repliée**, où les cercles sont superposés. Dans le mode **Eléments de légende séparés**, les cercles sont au-dessous les uns des autres, mais se retrouvent souvent tronqués
* On peut donner un titre à la légende, par exemple **Population**, par défaut il s'agit du nom de la couche
* Cochez la case **Taille manuelle des classes** pour définir vous-même quelles valeurs comportera la légende
* Cliquez ensuite sur le bouton **+** pour ajouter ces valeurs. On recommande généralement de mettre les valeurs minimales et maximales, ainsi qu'une ou deux valeurs intermédiaires. Ici, la valeur minimale étant de 1, elle n'est pas montrée. Notez que vous pouvez choisir quelle sera la valeur affichée dans la légende en modifiant l'étiquette !


Cliquer ensuite sur OK, fermez la fenêtre des propriétés. La légende est visible dans la liste des couches, et pourra également être affichée dans une [mise en page](10_02_mise_en_page.php "10_02_mise_en_page.php").



### Représenter des variables relatives à des surfaces : cartes choroplèthes


Une carte choroplèthe est une carte en aplats de couleurs. Les régions sont colorées selon une mesure statistique telle que la densité de population ou le revenu par habitant. Ce type de carte [ne peut donc être utilisé pour représenter des quantités ou des effectifs](https://neocarto.hypotheses.org/5717 "https://neocarto.hypotheses.org/5717"). Les variables continues doivent être [discrétisées](http://www.hypergeo.eu/spip.php?article374 "http://www.hypergeo.eu/spip.php?article374") pour produire des classes.



[![Exemple de carte choroplethe : carte de densité de population par commune, France métropolitaine, discrétisation par quantiles](illustrations/10_01_carte_choroplethe.jpg)](illustrations/10_01_carte_choroplethe.jpg "illustrations/10_01_carte_choroplethe.jpg")
Exemple de carte choroplèthe réalisée sous QGIS montrant la densité de population par commune en France métropolitaine, avec une discrétisation par quantiles.

#### Créer un champ de densité de population


La première étape consistera pour nous à créer un champ densité de population, rempli en fonction de la population et de la surface.



Ouvrez la table attributaire de *COMMUNE*, [passez en mode édition](05_02_points.php#V21 "05_02_points.php#V21") et ouvrez la [calculatrice de champ](07_02_calculer.php#VII21 "07_02_calculer.php#VII21").


Calculez dans un nouveau champ nommé **densite** de type **décimal** la densité de population en **nombre d'habitants par km²**.




Quelle formule utiliser pour cela ?


On peut utiliser **$area** pour calculer la surface. Les unités de la couche étant des mètres (couche projetée en Lambert 93), il faut diviser $area par 1 000 000 pour obtenir des km2.


Au final, la formule est donc : **"POPULATION" / ($area / 1000000)**



Quittez le mode édition. Vérifiez le contenu du champ densite.



[![Champ densité dans la table attributaire](illustrations/10_01_densite_res.jpg)](illustrations/10_01_densite_res.jpg "illustrations/10_01_densite_res.jpg")
densité des communes classées par code INSEE.


#### Faire varier la couleur des communes en fonction du champ densité


Maintenant que ce champ est créé et à jour, il est possible de faire varier la couleur des communes en fonction de la densité.



Pour faire varier la couleur des communes en fonction de la densité :


**Propriétés de la couche COMMUNE → rubrique Symbologie**



[![Choix des paramètres du style pour une carte choroplèthe en 5 classes par la méthode des quantiles](illustrations/10_01_choroplethe_fenetre.jpg)](illustrations/10_01_choroplethe_fenetre.jpg "illustrations/10_01_choroplethe_fenetre.jpg")

* Sélectionnez le style **Gradué** pour discrétiser les valeurs
* Choisissez la colonne **densite** créée précédemment (notez que l'on pourrait aussi cliquer sur le bouton Expression pour calculer ici la densité, sans créer de nouveau champ)
* Choisissez éventuellement une palette de couleur
* Sélectionnez un **mode de discrétisation** (quantile, intervalles égaux, Jenks) et un **nombre de classes**
* Cliquez sur **Classer** pour voir apparaître les classes avec les couleurs qui leur sont attribuées


Appliquez ensuite les changements. Vous pouvez tester différents modes de discrétisation et nombres de classes.


Pour voir l'effectif de chaque classe, clic droit sur le nom de la couche →
 [Afficher le nombre d'entités

![clic droit sur la couche, afficher le nombre d'entités](illustrations/10_01_menu_nb_entites.jpg)](#thumb "#thumb") (les nombres peuvent mettre un peu de temps à s'afficher avec une couche un peu lourde comme ici).


Pour un meilleur rendu, vous pouvez supprimer les bordures des communes en cliquant sur le symbole puis sur **Remplissage simple → Style de trait → Pas de ligne**.



[![Cliquer sur Modifier pour enlever les bordures](illustrations/10_01_enlever_bordure.jpg)](illustrations/10_01_enlever_bordure.jpg "illustrations/10_01_enlever_bordure.jpg")
[![Cliquer sur Modifier pour enlever les bordures](illustrations/10_01_enlever_bordure_02.jpg)](illustrations/10_01_enlever_bordure_02.jpg "illustrations/10_01_enlever_bordure_02.jpg")

Toutefois, même ainsi, les limites restent un peu visibles. Pour ne vraiment plus les voir, il faut rendre visibles ces limites avec une épaisseur fine et leur donner la même couleur que la couleur de remplissage.




[![Exemple de carte choroplethe : 5 classes, méthode des quantiles, dégradé de bleu](illustrations/10_01_choroplethe_visu.jpg)](illustrations/10_01_choroplethe_visu.jpg "illustrations/10_01_choroplethe_visu.jpg")

### Représenter des quantités ou des effectifs : cartes en semis de points


Une carte en semis de points permet, à partir d'un maillage surfacique, de représenter des quantités ou effectifs par des points placés aléatoirement au sein de chaque polygone. Le nombre de ces points est proportionnel à la quantité ou l'effectif lié au polygone.




Carte en semis de points des Etats-Unis : 1 point représente un personne, sa couleur est fonction de l'origine de cette personne. Cette carte met en lumière la ségrégation qui a lieu notamment dans certains quartiers des grandes villes.

Ici, nous allons créer ces points aléatoires en fonction du champ POPULATION. On pourrait créer un point par personne, mais le temps de création de la couche de points serait très long, et le résultat serait peu lisible. **Nous allons donc créer un point pour 100 personnes.**


Il faudra donc diviser la population par 100, et arrondir le résultat à l'entier le plus proche, puisqu'on ne peut créer 1,2 points.



Pour créer les points aléatoires :
 [Boîte à outils → Création de vecteurs → Points aléatoires à l'intérieur des polygones

![Emplacement de l'outil de points aléatoires à l'intérieur des polygones dans la boîte à outils](illustrations/10_01_pts_aleatoires_menu.jpg)](#thumb "#thumb")




[![Fenêtre de création des points aléatoires](illustrations/10_01_pts_aleatoires_fenetre.jpg)](illustrations/10_01_pts_aleatoires_fenetre.jpg "illustrations/10_01_pts_aleatoires_fenetre.jpg")

* Couche source : **COMMUNE**
* Stratégie d'échantillonnage : **Nombre de points**, pour créer un nombre de points directement proportionnel à la population
* Comptage de points : cliquez sur le bouton à droite, choisissez **éditer** et tapez l'expression suivante :  **round("POPULATION"/100)**, pour diviser la population par 100 et arrondir le résultat pour obtenir un nombre entier
* Laissez les autres paramètres par défaut, pour créer une couche temporaire
* **Exécuter**, patientez, l'opération est un peu longue... et fermez la fenêtre une fois terminé.


Ajustez le style de la couche, par exemple à l'échelle du pays :



[![paramètres de représentation de la couche de points](illustrations/10_01_style_pts_aleatoires.jpg)](illustrations/10_01_style_pts_aleatoires.jpg "illustrations/10_01_style_pts_aleatoires.jpg")



[![Exemple de carte en semis de points](illustrations/10_01_pts_aleatoires_visu.jpg)](illustrations/10_01_pts_aleatoires_visu.jpg "illustrations/10_01_pts_aleatoires_visu.jpg")

### Connaître la distribution de ses données


Il peut être utile pour mieux comprendre et représenter ses données de connaître leur distribution, par exemple avec un histogramme de fréquence. Ceci peut aider notamment à définir des classes pour une discrétisation.


Il est plus logique de faire cette étape avant de choisir un mode de représentation ; néanmoins, parce-qu'il est plus simple de l'aborder en sachant déjà discrétiser des données dans QGIS, cette partie arrive en fin de chapitre.


Nous allons voir 2 méthodes, une directement dans la fenêtre des propriétés de la couche, et l'autre avec l'extension Plotly.


Ici, nous allons prendre l'exemple de la densité de population pour les communes de France métropolitaine.



Si ce n'est pas déjà fait, ajoutez à votre projet la couche *[COMMUNE.shp](donnees/TutoQGIS_10_Representation.zip "donnees/TutoQGIS_10_Representation.zip")* située dans le dossier **TutoQGIS_10_representation/donnees**.



#### Histogramme simple


Il existe une méthode simple directement inclue dans QGIS pour avoir un aperçu de la distribution de vos données.



Ouvrez les propriétés de la couche de communes, et [choisissez le mode gradué](10_01_representation.php#X12b "10_01_representation.php#X12b") pour le champ densité [créé précédemment](10_01_representation.php#X12a "10_01_representation.php#X12a") avec une discrétisation par exemple par quantiles.


Cliquez ensuite sur l'onglet **Histogramme** (toujours dans la rubrique symbologie) puis sur **Charger les valeurs** :



[![Histogramme dans la fenêtres des propriétés](illustrations/10_01_histogramme.jpg)](illustrations/10_01_histogramme.jpg "illustrations/10_01_histogramme.jpg")


On ne voit pas grand chose... L'axe des x est créé en fonction des valeurs minimales et maximales, et la plupart des communes ayant une densité inférieure à 1000 habitants / km², elles ne sont pas visibles ici.


Les axes ne sont pas paramétrables et il n'est pas possible de zoomer, ce qui est une limite importante de cet outil. Testons néanmoins pour un jeu de données ne présentant pas de valeur maximale extrême, par exemple pour les communes de densité inférieure à 300 habitants/km².


Pour cela, nous allons [filtrer les données](01_02_info_geo.php#I23c "01_02_info_geo.php#I23c"), ce qui ne modifie pas la couche elle-même.



Toujours dans la fenêtre des propriétés, rendez-vous dans l'onglet **Source** et cliquez sur le bouton **Constructeur de requête** tout en bas de la fenêtre.


Filtrez uniquement les communes de densité < 300 habitants/km² avec la requête **"densite" < 300**. Cliquez ensuite sur **OK**.


Retournez dans la rubrique **Symbologie**, onglet **Classes** et cliquez sur le bouton **Classer** pour mettre à jour les classes. Dans l'onglet **Histogramme**, cliquez sur **Charger les valeurs** pour mettre à jour l'histogramme.



[![Histogramme de fréquence pour les communes de densite<300](illustrations/10_01_histogramme_filtre.jpg)](illustrations/10_01_histogramme_filtre.jpg "illustrations/10_01_histogramme_filtre.jpg")

On y voit plus clair ! Au passage, profitez-en pour cocher les cases **moyenne** et **écart-type**. Et vous pouvez ainsi vous rendre compte de l'intérêt principal de cet histogramme : les couleurs sont celles de la discrétisation choisie, et il est possible de modifier les bornes des classes directement dans l'histogramme.


Testez-le en faisant glisser un des traits correspondant à une borne. En cliquant sur le bouton **Appliquer**, les changements sont visibles dans la fenêtre de QGIS.


Ceci peut être très utile pour appliquer la méthode des **seuils observés** : délimiter les classes à la main, en se basant sur les ruptures visibles dans l'histogramme.


N'oubliez pas de **supprimer le filtre** pour travailler à nouveau sur l'ensemble de vos données.



#### Histogramme avec l'extension Plotly


Une autre méthode, permettant plus de souplesse au niveau du paramétrage de l'histogramme, mais n'étant pas liée à la discrétisation, consiste à utiliser l'extension [Plotly](https://github.com/ghtmtt/DataPlotly "https://github.com/ghtmtt/DataPlotly") créée par Matteo Ghetta (Faunalia).


Cette extension permet la création de graphiques de différents types (nuages de points, boîtes à moustaches, histogramme...) à partir des données chargées dans QGIS. Nous ne verrons pas ici toutes les fonctionnalités liées à cette extension, mais vous aurez une petite entrevue de ses riches possibilités !



Il faut tout d'abord [installer l'extension](03_04_fonds_carte.php#III43 "03_04_fonds_carte.php#III43") : **menu Extension → Installer/Gérer les extensions**, tapez **plotly** dans la barre de recherche et cliquez sur **Installer l'extension**.


![icône extension Plotly](illustrations/10_01_plotly_icone.jpg)Plotly est ensuite accessible via le **menu Extension → DataPlotly** ou bien en cliquant sur son icône.


Un nouveau panneau appraît : il peut être nécessaire de l'agrandir un peu.


Pour affficher un histogramme de fréquence de la densité de population :



[![Configuration de l'extension plotly pour afficher un histogramme de la densité de pop](illustrations/10_01_plotly_config.jpg)](illustrations/10_01_plotly_config.jpg "illustrations/10_01_plotly_config.jpg")

* Choisissez le type **Histogram**
* Les données à représenter proviennent de la couche **COMMUNE**...
* ...et de son champ **densite**
* Cliquez ensuite sur le bouton **Créer le graphique** tout en bas :



[![Exemple d'histogramme de fréquence pour la densité réalisé avec Plotly](illustrations/10_01_plotly_graphique_v1.jpg)](illustrations/10_01_plotly_graphique_v1.jpg "illustrations/10_01_plotly_graphique_v1.jpg")

La barre d'outils en haut à droite permet de zoomer, dézoomer etc. dans le graphique.


Tout est ensuite paramétrable, ou presque, notamment ici :



[![Paramétrage du graphique dans Plotly](illustrations/10_01_plotly_config1.jpg)](illustrations/10_01_plotly_config1.jpg "illustrations/10_01_plotly_config1.jpg")

Ou là :



[![Paramétrage du graphique dans Plotly](illustrations/10_01_plotly_config2.jpg)](illustrations/10_01_plotly_config2.jpg "illustrations/10_01_plotly_config2.jpg")

Pour appliquer les changements, il faut cliquer sur **Mettre à jour le graphique** en bas de la fenêtre.


Par exemple en diminuant la taille des barres et en zoomant :



[![Exemple d'histogramme de fréquence pour la densité réalisé avec Plotly](illustrations/10_01_plotly_graphique_v2.jpg)](illustrations/10_01_plotly_graphique_v2.jpg "illustrations/10_01_plotly_graphique_v2.jpg")

N'hésitez pas à tester les différents paramètres !


En-dessous du graphique, il y a 2 boutons pour l'exporter au format HTML (interactif) ou PNG (image).



En conclusion de ce chapitre, nous avons vu ici trois manières de représenter une même donnée : la population des communes. Il en existe beaucoup d'autres !


Dans le chapitre suivant, nous aborderons la **mise en page de cartes** afin par exemple de pouvoir les intégrer dans un article : ajout d'un titre, d'une légende... et export au format image ou vectoriel. L'export au format vectoriel vous permettra de retravailler la carte dans un logiciel de dessin vectoriel.




[chapitre précédent](10_00_carto.php "10_00_carto.php")
[chapitre suivant](10_02_mise_en_page.php "10_02_mise_en_page.php")


[haut de page](#wrap "#wrap")
