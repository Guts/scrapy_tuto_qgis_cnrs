
## III.3 Ajout de données ponctuelles à partir d'un fichier texte


* [Qu'y a-t-il dans le fichier texte ?](#III31 "#III31")
* [Visualisation des données dans QGIS](#III32 "#III32")
* [Création du shapefile de points](#III33 "#III33")


Nous avons vu quelques pistes pour rechercher et afficher des données au format SIG dans QGIS, que ce soit en les [téléchargeant](03_01_donnees_internet.php "03_01_donnees_internet.php") ou via des [flux](03_02_donnees_flux.php "03_02_donnees_flux.php"). Il arrive aussi de disposer d'un tableau avec deux colonnes X et Y : comment utiliser ces données dans un SIG ?


Nous prendrons ici l'exemple d'un fichier au [format CSV](http://fr.wikipedia.org/wiki/Comma-separated_values "http://fr.wikipedia.org/wiki/Comma-separated_values"). Pour information, il est possible de créer un fichier au format CSV à partir d'un fichier ODS (LibreOffice) ou XLS (Microsoft Office) par exemple.


### Qu'y a-t-il dans le fichier texte ?



Dans l'explorateur de votre ordinateur, ouvrez le fichier *[villes_bhutan_geonames.csv](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")* situé dans le dossier **TutoQGIS_03_RechercheDonnees/donnees** à l'aide d'un éditeur de texte simple (**pas dans un tableur**) : par exemple, WordPad dans Windows, TextEdit sous Mac, gedit sous Ubuntu.



[![capture d'écran du fichier CSV](illustrations/3_3_apercu_csv.jpg)](illustrations/3_3_apercu_csv.jpg "illustrations/3_3_apercu_csv.jpg")


Le format CSV est un format relativement simple : il contient des colonnes séparées habituellement par des virgules, parfois par des points-virgules, tabulations ou autre. La première ligne contient les en-têtes de colonnes.





Combien de colonnes y a-t-il dans le fichier *villes_bhutan_geonames.csv* ?


Le fichier comporte 9 colonnes : geonamesid, name, asciiname, latitude, longitude, country code, population, dem et modification date.


![capture d'écran des données du CSV avec les noms de colonnes encadrés en rouge](illustrations/3_3_csv_colonnes.jpg)





Quelle est la latitude de la ville de Timphu?


La latitude de la ville de Timphu est 27.46609 (la colonne "latitude" est la 4ème colonne : la réponse se trouve donc dans la 4ème colonne de la ligne correspondant à Timphu.


![capture d'écran des données du CSV avec la latitude de Timphu encadrée en rouge](illustrations/3_3_lat_timphu.jpg)





A quoi correspond la colonne "dem" ? Pouvez-vous trouver la réponse dans les métadonnées ?


Pour rappel, dans les données que vous avez téléchargées pour chaque partie, il existe dans le dossier **liste_donnees** une liste de ces données avec l'emplacement de leurs métadonnées.


En vous rendant sur [http://download.geonames.org/export/dump/readme.txt](http://download.geonames.org/export/dump/readme.txt "http://download.geonames.org/export/dump/readme.txt") dans un navigateur internet, vous pouvez lire la définition suivante pour la colonne dem (dans la partie "The main 'geoname' table has the following fields" ) : **digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.**


Il s'agit donc de la valeur d'un [modèle d'élévation numérique](http://fr.wikipedia.org/wiki/Mod%C3%A8le_num%C3%A9rique_de_terrain "http://fr.wikipedia.org/wiki/Mod%C3%A8le_num%C3%A9rique_de_terrain"), correspondant approximativement à l'altitude. Différents modèles ont été utilisés, à différentes résolutions.



Fermez le fichier sans enregistrer les éventuelles modifications, quittez l'éditeur de texte.



Ce fichier contient donc une liste de villes du [Bhoutan](http://fr.wikipedia.org/wiki/Bhoutan "http://fr.wikipedia.org/wiki/Bhoutan"), avec pour chaque ville différentes informations telles que sa population, son élévation, sa latitude et sa longitude.





A votre avis, dans quel SCR sont mesurées la latitude et la longitude? Pouvez-vous trouver cette info dans les métadonnées?


Comme précisé dans le fichier de métadonnées (voir fichier pdf dans le dossier liste_donnees), les coordonnées sont mesurées en degrés décimaux dans le SCR WGS84.


Dans le cas d'un fichier avec des coordonnées en latitude et longitude et un SCR inconnu, il s'agit fréquemment de coordonnées en WGS84.




### Visualisation des données dans QGIS



Ouvrez un nouveau projet vide dans QGIS.


![Icône ajout d'une couche vecteur](illustrations/1_2_gestionnaire_donnees_icone.jpg)Chargez la couche *[ne_10m_admin_0_countries.shp](donnees/TutoQGIS_03_RechercheDonnees.zip "donnees/TutoQGIS_03_RechercheDonnees.zip")* située dans le dossier **TutoQGIS_03_RechercheDonnees/donnees**.


![icône ajout fichier texte délimité](illustrations/1_2_gestionnaire_donnees_icone.jpg)Toujours à partir du gestionnaire des sources, cliquez sur **Texte délimité** :



[![Fenêtre d'ajout d'une couche CSV](illustrations/3_3_ajout_csv_fenetre.jpg)](illustrations/3_3_ajout_csv_fenetre.jpg "illustrations/3_3_ajout_csv_fenetre.jpg")

* Cliquez sur le bouton **...** et sélectionnez le fichier *villes_bhutan_geonames.csv*
* **Format de fichier :** choisir **CSV (virgule)**
* **Options des champs et enregistrements :** vérifiez que les cases **en-têtes de 1ère ligne**, **Détecter les types de champs** et **Virgule en sépareteur décimal** soient bien cochées
* **Définition de la géométrie :**  choisir **point**, puis les colonnes X et Y : **longitude et latitude**
* Vérifiez également que le SCR sélectionné soit bien **WGS84 - code EPSG 4326**


Cliquez sur **Ajouter**. Faites un clic droit sur le nom de cette couche, **zoomer sur la couche**.



[![Visualisation des villes du bhutan et de leurs données attributaires sous QGIS](illustrations/3_3_visu_villes_bhutan.jpg)](illustrations/3_3_visu_villes_bhutan.jpg "illustrations/3_3_visu_villes_bhutan.jpg")

Les villes ont bien été ajoutées à QGIS sous la forme d'une couche de points.



### Création du shapefile de points


Regardez [à quel emplacement](01_02_info_geo.php#I23b "01_02_info_geo.php#I23b") est stockée votre couche. Vous pouvez observer que cet emplacement fait référence à un fichier CSV et non à un fichier SHP.


Par ailleurs, si vous sélectionnez la couche de villes dans la table des matières, vous pouvez constater que l'icône pour passer en mode édition est désactivée, au contraire de notre couche de pays. La couche de villes n'est donc pas éditable.


Icône édition activée : ![Icône édition activée](illustrations/3_3_edition_icone_activee.jpg) Icône édition désactivée : ![Icône édition désactivée](illustrations/3_3_edition_icone_desactivee.jpg)


Ces indices laissent à penser que bien que nous puissions visualiser les villes dans QGIS, **aucune couche n'a été créée sur votre ordinateur**, ce qui est d'ailleurs logique dans la mesure où QGIS ne nous a demandé à aucun moment de choisir un emplacement pour cette couche.


En fait, nous avons seulement créé **une couche temporaire, uniquement stockée dans le projet QGS en cours**. Comment faire pour sauvegarder cette couche?



Il suffit pour cela de faire un
 [clic-droit sur la couche *villes_bhutan_geonames* → Exporter → Sauvegarder les entités sous...

![clic droit sur la couche, sauvegarder sous](illustrations/3_3_sauvegarder_villes_menu.jpg)](#thumb "#thumb")




[![fenêtre de sauvegarde de la couche](illustrations/3_3_sauvegarder_villes_fenetre.jpg)](illustrations/3_3_sauvegarder_villes_fenetre.jpg "illustrations/3_3_sauvegarder_villes_fenetre.jpg")

* choisissez le format : **GeoPackage**
* Cliquez sur **...** pour sélectionner l'emplacement où la couche sera créée et lui donner un nom
* Laissez les autres paramètres par défaut


Cliquez sur **OK** ; la couche est ajoutée à QGIS, vous devez donc avoir deux couches de villes identiques au premier abord ; cependant, l'une est temporaire et l'autre permanente.


![Icône supprimer une couche](illustrations/3_3_supprimer_couche_icone.jpg)
[Supprimez la couche temporaire

![clic-droit sur la couche, supprimer](illustrations/3_3_supprimer_couche_menu.jpg)](#thumb "#thumb")
 pour éviter toute confusion (en vous aidant éventuellement de son emplacement pour déterminer laquelle est-ce).




Félicitations ! L'ajout de données ponctuelles à partir d'un fichier texte dans QGIS n'a désormais plus de secrets pour vous !


Notez que si vous effectuez cette manipulation avec un fichier CSV « non standard » (dont le délimiteur n'est pas la virgule), il vous faudra choisir l'option **délimiteurs personnalisés** dans la fenêtre d'ajout du fichier CSV, puis votre délimiteur : point-virgule, tabulation... Attention aussi à la case **Virgule en séparateur décimal**, à cocher ou décocher suivant vos coordonnées (44,192 vs 44.192).




[chapitre précédent](03_02_donnees_flux.php "03_02_donnees_flux.php")
[chapitre suivant](03_04_fonds_carte.php "03_04_fonds_carte.php")


[haut de page](#wrap "#wrap")
