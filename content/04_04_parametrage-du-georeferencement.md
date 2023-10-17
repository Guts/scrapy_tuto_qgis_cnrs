
## IV.4 Paramétrage du géoréférencement


* [Type de transformation, ou comment calculer les nouvelles coordonnées des points ?](#IV41 "#IV41")
	+ [Qu'est-ce qu'une transformation ?](#IV41a "#IV41a")
	+ [Quelques types de transformations](#IV41b "#IV41b")
	+ [Choisir une transformation](#IV41c "#IV41c")
* [Rééchantillonnage, ou comment calculer les valeurs des pixels ?](#IV42 "#IV42")
* [Mode de compression utilisé pour la création de la nouvelle image](#IV43 "#IV43")
* [Raster en sortie et SCR](#IV44 "#IV44")
	+ [Raster de sortie](#IV44a "#IV44a")
	+ [SCR cible](#IV44b "#IV44b")
* [Les autres paramètres](#IV45 "#IV45")
	+ [Enregistrer les points de contrôle](#IV45a "#IV45a")
	+ [Transparence](#IV45b "#IV45b")
	+ [Définir la résolution de la cible](#IV45c "#IV45c")
	+ [Carte et rapport PDF](#IV45d "#IV45d")
	+ [Charger directement le raster dans QGIS](#IV45e "#IV45e")
* [Une fois tous les paramètres choisis...](#IV46 "#IV46")




Avant de pouvoir procéder au géoréférencement proprement dit, il va nous falloir définir plusieurs paramètres.



![Icône paramètres de transformation du géoréférenceur](illustrations/4_4_parametres_icone.jpg)Ces paramètres sont accessibles dans le menu
 [Paramètres → Paramètres de transformation

![Menu Paramètres, Paramètres de transformation](illustrations/4_4_parametres_menu.jpg)](#thumb "#thumb")
 ou bien en cliquant sur l'icône correspondante.



[![Fenêtre de saisie des paramètres de transformation](illustrations/4_4_parametres_fenetre.jpg)](illustrations/4_4_parametres_fenetre.jpg "illustrations/4_4_parametres_fenetre.jpg")


Nous allons passer en revue ces différents paramètres.


### Type de transformation, ou comment calculer les nouvelles coordonnées des points ?


#### Qu'est-ce qu'une transformation ?


Lors du calage, l'image subit une transformation, afin de faire coïncider au maximum les points de départ avec les coordonnées spécifiées par l'utilisateur. Une transformation est en fait une formule mathématique transformant les coordonnées de départ vers les coordonnées voulues.


Il existe divers types de transformations, adaptées à des usages différents. Chaque transformation, si on l'utilise avec un nombre de points de calage supérieur à son minimum, renverra une erreur correspondant à la différence entre les coordonnées "idéales" voulues par l'utilisateur et les coordonnées effectivement calculées lors de la transformation (erreur résiduelle **residual[pixels]** de la table des points de contrôle, voir plus haut).


#### Quelques types de transformations


QGIS permet les transformations suivantes :


* **linéaire** (2 points minimum) : type le plus simple, ne déforme pas le raster. Cette transformation est rarement suffisante pour des images scannées.
* **Helmert** (2 points minimum) : cas particulier de transformation polynomiale d'ordre 1.
* **transformation polynomiale d'ordre 1**, ou transformation affine (3 points minimum) : elle préserve la colinéarité (3 points alignés le resteront) et permet seulement changement d'échelle, translation et rotation.
* **transformation polynomiale d'ordre 2** (6 points minimum) : permet une distorsion du raster.
* **transformation polynomiale d'ordre 3** (10 points minimum) : le degré de distorsion possible est plus important que pour une transformation d'ordre 2.
* **Thin Plate Spline (TPS)** (1 point minimum) : méthode récente, permettant de prendre en compte des déformations locales. Cette transformation est utile lorsqu'on dispose d'originaux de très mauvaise qualité.
* **projective** (4 points minimum) : une des transformations les plus complexes, qui ne conserve pas le parallélisme. Un carré sera transformé en quadrilatère.


#### Choisir une transformation


Quelques éléments vous ont été donnés dans la description des types de transformation pouvant vous aider à choisir l'une ou l'autre transformation. En pratique, le choix est souvent difficile et requiert de tester plusieurs transformations et de les comparer si l'on recherche une bonne précision.


Ici, nous nous bornerons à choisir une transformation simple et rapide.



Sélectionnez la transformation **polynomiale 1** dans la liste déroulante de la fenêtre de paramétrage.



[![Choix du type de transformation](illustrations/4_4_type_transfo.jpg)](illustrations/4_4_type_transfo.jpg "illustrations/4_4_type_transfo.jpg")


### Rééchantillonnage, ou comment calculer les valeurs des pixels ?


Si on utilise une transformation qui déforme le raster d'origine (transformation polynomiale d'ordre supérieur à 1, ou transformation de type Spline par exemple), la valeur (couleur) de chaque pixel du nouveau raster sera déterminée par un calcul en se basant sur le raster original.


Cette valeur sera différente selon la méthode de rééchantillonnage choisie. QGIS, comme d'autres logiciels SIG, propose trois méthodes de rééchantillonnage :



[![3 types de rééchantillonnage](illustrations/4_4_resampling.svg)](illustrations/4_4_resampling.svg "illustrations/4_4_resampling.svg")

* **Plus proche voisin :** le nouveau pixel prend la valeur du pixel de l'ancien raster le plus proche. Cette méthode est la plus rapide, et est utilisée principalement pour des données catégorisées (occupation du sol par exemple) puisqu'elle ne crée pas de nouvelles valeurs.
* **Linéaire :** la valeur du nouveau pixel est déterminée à partir des valeurs des 4 pixels les plus proches. Cette méthode est utilisée pour des données continues et permet un lissage du raster.
* **Cubique :** la valeur du nouveau pixel est déterminée à partir des valeurs des 16 pixels les plus proches. Ceci provoque moins de distorsion géométrique de l'image mais nécessite un temps de calcul relativement long. Par ailleurs, il y a plus de possibilités d'obtenir avec cette méthode de nouvelles valeurs de pixel par rapport aux valeurs de départ.


Il est aussi possible de choisir les méthodes **Cubic Spline** et **Lanczos**, mais au-delà du fait que ce sont des méthodes plus complexes que les précédentes, je ne saurais pas les expliquer et encore moins leurs avantages et inconvénients ! A vous de tester...


Le choix d'une méthode de rééchantillonnage a surtout une influence dans le cas où la taille des pixels est importante par rapport à la taille des objets qui seront étudiés sur l'image, par exemple une photo aérienne où chaque maison est constituée de seulement quelques pixels.


Dans notre cas (carte scannée avec une bonne résolution), le choix du type de rééchantillonnage influencera peu le résultat.



Ici, nous allons donc choisir la méthode la plus simple et la plus rapide : **plus proche voisin**.



[![Choix du type de rééchantillonnage](illustrations/4_4_reechantillonnage.jpg)](illustrations/4_4_reechantillonnage "illustrations/4_4_reechantillonnage")


### Mode de compression utilisé pour la création de la nouvelle image


La compression permet d'obtenir un raster moins volumineux, mais peut provoquer une perte de qualité. Une image compressée peut par ailleurs être illisible par certains logiciels.


QGIS propose les méthodes suivantes :


* **Aucun :** pas de compression
* **LZW :** utilisé pour les images au format GIF et TIF. Assez largement utilisé, permet une compression jusqu'au 1:10
* **PACKBITS :** offre une compression moindre que la méthode LZW, mais ce format est plus courant
* **DEFLATE :** similaire à LZW, mais principalement prise en charge par les logiciels Adobe



Notre image de base étant peu volumineuse, nous allons choisir le type **Aucun**.



[![Choix du type de compression](illustrations/4_4_compression.jpg)](illustrations/4_4_compression.jpg "illustrations/4_4_compression.jpg")


### Raster en sortie et SCR


#### Raster de sortie



Spécifiez ici le nom et l'emplacement de l'image géoréférencée qui sera créée, en cliquant sur l'icône à droite de la ligne **Raster de sortie**.



[![Choisir le nom et l'emplacement du raster de sortie](illustrations/4_4_raster_sortie.jpg)](illustrations/4_4_raster_sortie.jpg "illustrations/4_4_raster_sortie.jpg")

Choisissez à quel endroit vous souhaitez créer cette couche, et donnez-lui un nom, par exemple **Oahu_Hawaiian_Islands_1906_pol1_wgs84.tif**.



#### SCR cible


Comme décidé en partie [précédemment](04_02_preliminaires.php#IV22 "04_02_preliminaires.php#IV22"), nous allons partir du principe que les coordonnées de cette carte sont exprimées dans un système proche du WGS84.



Cliquez sur l'icône à droite de la ligne **SCR cible**, ou bien utilisez la liste déroulante pour choisir directement le SCR.



[![Choisir le SCR](illustrations/4_4_choisir_scr.jpg)](illustrations/4_4_choisir_scr.jpg "illustrations/4_4_choisir_scr.jpg")

Choisissez le SCR **WGS 84, code EPSG 4326**, en vous aidant éventuellement de la partie filtre.



[![Sélection du SCR WGS84](illustrations/4_4_choix_scr_fenetre.jpg)](illustrations/4_4_choix_scr_fenetre.jpg "illustrations/4_4_choix_scr_fenetre.jpg")


### Les autres paramètres


#### Enregistrer les points de contrôle


Si vous n'avez pas déjà enregistré les points de contrôle, ça peut être une bonne idée de cocher cette case afin de sauvegarder votre travail, et de garder trace des points utilisés, pour tester ensuite avec une autre transformation par exemple.


#### Transparence


Employer 0 pour la transparence : cette option est utile principalement pour les photographies aériennes ou satellites et permet de ne pas visualiser les pixels noirs (bords de l'image), ce qui serait gênant dans notre cas.



Laissez cette case décochée.



[![employer 0 pour la transparence : la case est décochée](illustrations/4_4_transparence.jpg)](illustrations/4_4_transparence.jpg "illustrations/4_4_transparence.jpg")


#### Définir la résolution de la cible



Laisser cette case décochée pour que l'image créée ait la même résolution que l'image de départ.



[![résolution de la cible : la case est décochée](illustrations/4_4_resolution.jpg)](illustrations/4_4_resolution.jpg "illustrations/4_4_resolution.jpg")


#### Carte et rapport PDF


La carte PDF permettra de visualiser le décalage qu'aura subi chaque point de contrôle. Le rapport PDF comportera notamment les coordonnées et erreurs pour chaque point.



Cliquez sur les icônes à droite des lignes carte PDF et rapport PDF pour spécifier un nom (à votre convenance) et l'emplacement (par exemple dans le même dossier que l'image de départ) pour la carte et le rapport qui seront créés.



[![icônes pour choisir le nom et l'emplacement de la carte et du rapport PDF](illustrations/4_4_carte_rapport_icone.jpg)](illustrations/4_4_carte_rapport_icone.jpg "illustrations/4_4_carte_rapport_icone.jpg")


#### Charger directement le raster dans QGIS



Charger dans QGIS lorsque terminé : cocher cette case pour que le nouveau raster soit chargé automatiquement dans QGIS une fois le géoréférencement effectué.



[![charger dans qgis : la case est cochée](illustrations/4_4_charger_dans_qgis.jpg)](illustrations/4_4_charger_dans_qgis.jpg "illustrations/4_4_charger_dans_qgis.jpg")


### Une fois tous les paramètres choisis...


...Cliquez sur OK : les paramètres sont sauvegardés... Mais rien ne semble se passer. Rendez-vous dans la partie suivante pour l'étape finale !




[chapitre précédent](04_03_calage_carroyage.php "04_03_calage_carroyage.php")
[chapitre suivant](04_05_lancement.php "04_05_lancement.php")


[haut de page](#wrap "#wrap")
