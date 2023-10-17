
## XI.1 Traitement de base pour une seule couche


Nous allons (re)voir ici une manipulation simple : comment [découper une couche par une autre](09_01_vecteur.php#IX11 "09_01_vecteur.php#IX11").


Nous verrons dans les chapitres suivants comment **automatiser ce traitement**, pour par exemple découper rapidement 10 couches par une autre.



Lancer QGIS et ouvrir le projet *[decoupe.qgz](donnees/TutoQGIS_11_Automatisation.zip "donnees/TutoQGIS_11_Automatisation.zip")* situé dans **TutoQGIS_11_automatisation/projets**.


Ce projet contient une couche correspondant aux limites communales de la commune de Sainte-Radégonde, ainsi que 4 autres couches de lieux, routes, espaces naturels et bâtiments.



[![Aperçu du projet decoupe.qgz](illustrations/11_01_projet.jpg)](illustrations/11_01_projet.jpg "illustrations/11_01_projet.jpg")



Vérifier que toutes les couches aient bien le même SCR. Quel est ce SCR ?


En allant dans les propriétés de chaque couche, rubrique Source (ou bien en survolant le nom de chaque couche et en lisant l'infobulle), on peut constater qu'elles sont toutes en RGF93/Lambert 93, code EPSG 2154.



Pour découper la couche de routes par la commune :
 [Boîte à outils → Recouvrement de vecteur → Couper

![Emplacement de l'outil Couper dans la boîte à outils](illustrations/11_01_couper_menu.jpg)](#thumb "#thumb")




[![Fenêtre de l'outil Couper](illustrations/11_01_decouper_fenetre.jpg)](illustrations/11_01_decouper_fenetre.jpg "illustrations/11_01_decouper_fenetre.jpg")

Une nouvelle couche temporaire est créée, qui ne contient que les portions de routes à l'intérieur de la commune.



Comment faire maintenant pour découper les 4 couches par la commune, sans répéter 4 fois cette opération ?




[chapitre précédent](11_00_automatisation.php "11_00_automatisation.php")
[chapitre suivant](11_02_par_lot.php "11_02_par_lot.php")


[haut de page](#wrap "#wrap")
