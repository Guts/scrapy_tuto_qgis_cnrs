
## XI.4 Comprendre et lancer un script Python

* [Lancer une commande Python dans QGIS](#XI41 "#XI41")
* [Ouvrir un script Python](#XI42 "#XI42")
* [Paramétrer le script](#XI43 "#XI43")
* [Lancer et éditer un script](#XI44 "#XI44")

Chaque manipulation que nous faisons dans QGIS via l'interface graphique (ajouter une couche, découper une couche etc.) peut également être faite sous forme d'une ligne de commande dans le langage [Python](https://fr.wikipedia.org/wiki/Python_%28langage%29 "https://fr.wikipedia.org/wiki/Python_%28langage%29").

Par exemple, pour ajouter la couche *SAINTE_RADEGONDE.shp*, située dans le dossier /mnt/travail/temp, vous pouvez soit l'ajouter comme nous l'avons fait jusqu'ici, soit taper la commande Python suivante :

qgis.utils.iface.addVectorLayer("/mnt/travail/temp/SAINTE_RADEGONDE.shp", "SAINTE_RADEGONDE", "ogr")

Ce qui revient à lancer l'outil d'ajout de couche vecteur **addVectorLayer** de QGIS, avec 3 paramètres :

* l'emplacement de la couche : **/mnt/travail/temp/SAINTE_RADEGONDE.shp** (ce chemin va bien sûr varier)
* le nom avec lequel la couche sera affichée dans QGIS : **SAINTE_RADEGONDE**
* le nom du fournisseur de données : **ogr** car QGIS utilise en interne une [bibliothèque](https://fr.wikipedia.org/wiki/Biblioth%C3%A8que_logicielle "https://fr.wikipedia.org/wiki/Biblioth%C3%A8que_logicielle") nommée ogr pour accéder aux shapefiles

Quel est l'intérêt ? D'abord, mieux comprendre comment fonctionne le logiciel. Ensuite, **créer exactement l'outil dont vous avez besoin**, avec plus de souplesse et de possibilités qu'un [modèle](11_03_modeleur.php "11_03_modeleur.php") ! Bien sûr, **on peut parfaitement utiliser QGIS sans jamais lire une ligne de Python**. Il s'agit d'un autre mode d'utilisation de QGIS.

Qu'allons-nous voir dans ce chapitre ? Il ne s'agit pas ici d'apprendre à coder en Python, mais simplement **d'ouvrir un script Python existant, voir comment est constitué ce script, comment le paramétrer et le lancer**. En quelque sorte une introduction à cette face cachée de QGIS !

### Lancer une commande Python dans QGIS

Rendez-vous dans le menu **Extension → Console Python**.

La console s'ouvre en bas de la fenêtre de QGIS. Dans cette console, vous pouvez taper des commandes Python qui seront exécutées une à une.

Tapez **print ('hello !')** en bas de la console :

[![test de la console : taper une commande](illustrations/11_04_test_console.jpg)](illustrations/11_04_test_console.jpg "illustrations/11_04_test_console.jpg")

Puis appuyez sur la touche entrée. Vous devriez voir votre commande, suivie du résultat, en haut de la console :

[![test de la console : taper une commande](illustrations/11_04_test_console_resultat.jpg)](illustrations/11_04_test_console_resultat.jpg "illustrations/11_04_test_console_resultat.jpg")

Vous venez d’utiliser la commande **Print**, qui permet d'afficher du texte dans la console. Vous pouvez également tester la commande citée plus haut pour ajouter une couche vecteur :

qgis.utils.iface.addVectorLayer("/mnt/travail/temp/SAINTE_RADEGONDE.shp", "SAINTE_RADEGONDE", "ogr")

Il faut remplacer le chemin ("/mnt/travail/temp/SAINTE_RADEGONDE.shp") par le chemin vers la couche sur votre ordinateur.

Sur Windows, les chemins seront de la forme 'C:/…' par exemple.

Il est possible de travailler uniquement en lançant ainsi des commandes une à une ; seulement, les commandes utilisées ne seront pas sauvegardées et ne pourront donc être réutilisées sans tout retaper à la main (même s'il est possible de faire défiler les dernières commandes utilisées en appuyant sur la touche flèche haut du clavier).

### Ouvrir un script Python

Pour sauvegarder et réutiliser facilement votre travail, le plus simple est d'utiliser ce qu'on appelle un script. Il s'agit simplement d'un fichier texte comportant une suite de commandes, et qui porte l'extension PY puisqu'il s'agit d'un script Python.

Ce tutoriel n'étant pas un tutoriel Python, nous nous contenterons d'ouvrir un script existant plutôt que d'en créer un nous-mêmes.

![icône Afficher l'éditeur](illustrations/11_04_editeur_icone.jpg)Pour ouvrir un script : cliquez sur l'icône **Afficher l'éditeur** de la console : l'éditeur de script s'ouvre.

[![console Python avec l'icône Afficher l'éditeur](illustrations/11_04_editeur.jpg)](illustrations/11_04_editeur.jpg "illustrations/11_04_editeur.jpg")

Redimensionnez éventuellement la fenêtre, pour que la partie éditeur, à droite, soit suffisamment large, et que la hauteur soit suffisante.

![icône d'ouverture de script](illustrations/11_04_ouvrir_script_icone.jpg)Dans l'éditeur, cliquez sur l'icône **Ouvrir le script...** et allez chercher le script [clip_and_reproject.py](donnees/TutoQGIS_11_Automatisation.zip "donnees/TutoQGIS_11_Automatisation.zip") situé dans **TutoQGIS_11_Automatisation/scripts**.

[![Editeur Python avec l'icône d'ouverture de script](illustrations/11_04_ouvrir_script.jpg)](illustrations/11_04_ouvrir_script.jpg "illustrations/11_04_ouvrir_script.jpg")

Lisez le contenu du script. **Les lignes commençant par un # sont des commentaires** : leur contenu ne sera pas pris en compte, ils sont uniquement utiles pour mieux comprendre le script.

L'objectif n'est pas de comprendre dans le détail tout ce que fait ce script, mais de comprendre globalement ce qui s'y passe, notamment au moyen des commentaires. Il s'agit ici d'un script faisant le même travail que le modèle que vous avez réalisé en [précédemment](11_03_modeleur.php#XI33b "11_03_modeleur.php#XI33b"), à savoir découper plusieurs couches par une même couche et reprojeter les couches obtenues en WGS84.

### Paramétrer le script

Au début du script (ligne 15), vous trouverez ces lignes :

[![lignes du script correspondant aux paramètres en entrée](illustrations/11_04_parametres.jpg)](illustrations/11_04_parametres.jpg "illustrations/11_04_parametres.jpg")

Il s'agit des paramètres en entrée et sortie du script :

* **dossier_entree** : le dossier où sont situées les couches à découper
* **couche_masque** : la couche qui servira de masque de découpe
* **dossier_sortie** : le dossier où seront enregistrées les couches créées (ce dossier doit déjà exister)

A vous de modifier ces paramètres suivant l'emplacement des données sur votre ordinateur ! Attention à ce que le dossier en entrée ne comporte que les couches à découper.

Attention à bien écrire les chemins exacts dans le script, une erreur d'une seule lettre vous renverra un message d'erreur quand vous voudrez l'exécuter.

### Lancer et éditer un script

Pour savoir comment appeler un outil en python, une astuce est de d'abord le lancer « normalement » puis d'aller dans le **menu Traitement → Historique** et cliquer sur la ligne correspondante. En bas de la fenêtre, vous aurez la commande Python qui a été exécutée cette fois-là :

[![Fenêtre Historique](illustrations/11_04_historique.jpg)](illustrations/11_04_historique.jpg "illustrations/11_04_historique.jpg")

Comme indiqué [ici](09_01_vecteur.php#IX14 "09_01_vecteur.php#IX14"), l'historique est aussi très utile pour relancer rapidement un outil avec exactement les mêmes paramètres que la fois précédente, il suffit de double-cliquer sur la ligne correspondante !

[![icône exécuter le script dans la barre d'outil de l'éditeur de scripts](illustrations/11_04_executer_script_icone.jpg)](illustrations/11_04_executer_script_icone.jpg "illustrations/11_04_executer_script_icone.jpg")

Pour lancer le script, cliquez sur l'icône **Lancer le script** en haut de l'éditeur. Vérifiez que tout ait bien fonctionné.

Quelles modifications apporter au script pour que :

les couches soient reprojetées non plus en WGS84 mais en NTF / Lambert zone II (code EPSG 27572) ?

Ligne 64, remplacer **'EPSG:4326'** par **'EPSG:27572'**. Vous pouvez également remplacer ligne 62 **'_wgs84.shp'** par **'_ntfl2.shp'** (il s'agit du suffixe qui sera ajouté au nom de la nouvelle couche).

au lieu de l'outil Clip de découpage, ce soit l'outil Intersection qui soit utilisé ?

Ligne 46 remplacez **native:clip** par ce nom : **native:intersection**. Pour en savoir plus, vous pouvez voir [ici](https://docs.qgis.org/testing/en/docs/user_manual/processing/console.html#using-processing-algorithms-from-the-console "https://docs.qgis.org/testing/en/docs/user_manual/processing/console.html#using-processing-algorithms-from-the-console").

Pour en savoir plus sur le sujet, vous pouvez lire par exemple [ici](https://docs.qgis.org/latest/fr/docs/pyqgis_developer_cookbook/intro.html "https://docs.qgis.org/latest/fr/docs/pyqgis_developer_cookbook/intro.html").

[chapitre précédent](11_03_modeleur.php "11_03_modeleur.php")

[haut de page](#wrap "#wrap")
