
## IV.3 Points de calage : avec un carroyage

* [Création du premier point](#IV31 "#IV31")
* [Quelques astuces pour créer les points suivants](#IV32 "#IV32")

Nous allons créer ici des points de calage, c'est-à-dire attribuer leurs coordonnées à plusieurs points de l'image.

Pour ce faire, nous utiliserons la [première méthode décrite dans la partie IV.1](04_01_principe.php#IV12a "04_01_principe.php#IV12a") : nous nous baserons sur le carroyage de cette carte pour créer les points de calage (la deuxième méthode sera abordée dans la  [partie IV.6](04_06_calage_autre_couche.php "04_06_calage_autre_couche.php")).

### Création du premier point

Lancez QGIS ou créez un nouveau projet, et assurez-vous que le [SCR de ce projet](02_03_couches_projets.php#II31 "02_03_couches_projets.php#II31") soit le **WGS84 EPSG 4326**.

**Il est inutile d'ajouter la carte d'Oahu à QGIS** (si vous le faites néanmoins, profitez-en pour observer qu'en l'absence d'informations de localisation pour cette image, QGIS positionne son coin supérieur gauche aux coordonnées (0,0)).

![icône du géoréférenceur](illustrations/4_3_georeferenceur_icone.jpg)
 Ouvrez la fenêtre du géoréférenceur :
 [Menu Raster → Géoréférencer...

![Menu Raster, Géoréférencer, Géoréférencer...](illustrations/4_3_georeferenceur_menu.jpg)](#thumb "#thumb")

[![Fenêtre du géoréférenceur](illustrations/4_3_georeferenceur_fenetre.jpg)](illustrations/4_3_georeferenceur_fenetre.jpg "illustrations/4_3_georeferenceur_fenetre.jpg")

Il est possible d'afficher le géoréferenceur comme une fenêtre à part ou ancrée. Pour changer de mode, dans la fenêtre du géoréférenceur, **menu Paramètres → Configurer le géoréférenceur...**, cochez ou décochez la case **Afficher la fenêtre de géoréférencement dans la fenêtre principale**.

![icône ouvrir un raster du géoréférenceur](illustrations/4_3_ouvrir_raster_icone.jpg)Dans cette fenêtre, ajoutez au géoréférenceur l'image à caler en cliquant sur l'icône **Ouvrir un raster**, ou bien
 [menu Fichier → Ouvrir raster...

![Menu Fichier, ouvrir un raster](illustrations/4_3_ouvrir_raster_menu.jpg)](#thumb "#thumb")
 .

Sélectionnez la carte de l'île d'Oahu : fichier *[Oahu_Hawaiian_Islands_1906.jpg](donnees/TutoQGIS_04_Georef.zip "donnees/TutoQGIS_04_Georef.zip")*.

Selon votre version de QGIS, une fenêtre peut s'ouvrir pour demander le SCR de l'image ; puisque nous avons décidé de partir du principe que les coordonnées de cette carte était en WGS84,
 [choisissez ce SCR

![Choix du SCR WGS84 en utilisant le filtre 4326](illustrations/4_3_choix_scr_wgs84.jpg)](#thumb "#thumb")
 .

La carte s'affiche dans la fenêtre du géoréférenceur.

Il s'agit maintenant de renseigner les coordonnées de plusieurs points, en se basant sur les indications de la carte. Vous pouvez par exemple commencer par le point en haut à gauche :

[![emplacement du premier point de calage à créer](illustrations/4_3_premier_point.jpg)](illustrations/4_3_premier_point.jpg "illustrations/4_3_premier_point.jpg")

![icône d'ajout de point du géoréférenceur](illustrations/4_3_ajout_point_icone.jpg)Vérifiez que l'icône **Ajouter un point** soit bien sélectionnée et cliquez à l'intersection des deux lignes du carroyage :

[![Fenêtre de saisie des coordonnées d'un point de calage](illustrations/4_3_ajout_point_fenetre.jpg)](illustrations/4_3_ajout_point_fenetre.jpg "illustrations/4_3_ajout_point_fenetre.jpg")

Comment saisir les coordonnées de ce point ?

Ce point est situé aux coordonnées -158° 15' Est (longitude négative car le point est à l'ouest du méridien de Greeenwich) et 21° 40' Nord (latitude positive car le point est au Nord de l'équateur).

QGIS propose de saisir les coordonnées en degrés minutes secondes sous la forme dd mm ss.ss. Ici, nous avons juste des degrés et des minutes : le point a donc pour coordonnées **-158 15** Est et **21 40** Nord.

[![Fenêtre de saisie des coordonnées d'un point de calage, coordonnées remplies](illustrations/4_3_ajout_point_fenetre_rempli.jpg)](illustrations/4_3_ajout_point_fenetre_rempli.jpg "illustrations/4_3_ajout_point_fenetre_rempli.jpg")

Depuis la version 3.22, le choix du SCR se fait directement dans cette fenêtre de saisie d'un point. Vérifiez que le SCR sélectionné soit bien le WGS84, puis cliquez sur **OK**.

Le point apparaît sous forme d'une ligne dans la table des points de contrôle, sous la carte dans la fenêtre géoréférenceur :

[![Table des points de contrôle : premier point](illustrations/4_3_table_points.jpg)](illustrations/4_3_table_points.jpg "illustrations/4_3_table_points.jpg")

Que signifient les différentes colonnes de cette table ?

* **Visible :** indique si le point sera pris en compte ou non pour le géoréférencement. Permet de ne pas prendre en compte certains points qui semblent apporter trop d'erreurs, tout en les gardant en mémoire.
* **ID :** identifiant du point. Peut aider à repérer de quel point il s'agit sur la carte, dans le fenêtre du géoréférenceur comme dans celle de QGIS.
* **Source X et Y :** coordonnées du point dans l'image non géoréférencée, c'est-à-dire en considérant que le pixel en haut à gauche de l'image a pour coordonnées 0,0.
* **Destination X et Y :** les coordonnées que l'on souhaite faire prendre à ce point, exprimées dans le SCR choisi précédemment. Ces coordonnées sont en degrés décimaux (ici, -158°15' a été converti en -158,25 degrés décimaux).
* **dX (pixels) et dY (pixels) :** la différence entre les coordonnées qu'on souhaiterait voir prendre le point (dstX et dstY) et les coordonnées que prendra effectivement le point après le géoréférencement. En effet, en fonction du type de transformation choisi et du nombre de points de calage, il n'est pas toujours possible de faire coïncider exactement les points avec les coordonnées souhaitées.
* **Résidu (pixels) :** l'erreur associée à ce point, calculée à partir de dX[pixels] et dY[pixels]. Cette erreur est égale à la racine de la somme des carrés de dX[pixels] et dY[pixels], soit :  
√ ( dX[pixels] ² + dY[pixels] ² )

Dans notre table, les colonnes dX[pixels], dY[pixels] et residual[pixels] ne sont pas encore remplies, car nous n'avons pas encore défini le type de **transformation** à effectuer lors du géoréférencement. Cette notion sera abordée dans la [partie suivante](04_04_parametrage.php "04_04_parametrage.php"). En attendant, continuons à ajouter des points de calage pour en avoir par exemple six.

### Quelques astuces pour créer les points suivants

Procédez de la même manière pour rajouter 5 autres points de calage. Faites en sorte que ces points soient bien répartis sur l'image.

Pour visualiser les identifiants et/ou les coordonnées des points sur la carte du géoréférenceur :
 [Menu Paramètres → Configurer le géoréférenceur

![Menu Paramètres, Configurer le géoréférenceur](illustrations/4_3_config_georeferenceur_menu.jpg)](#thumb "#thumb")
 :

[![Fenêtre de configuration du géoréférenceur](illustrations/4_3_config_georeferenceur_fenetre.jpg)](illustrations/4_3_config_georeferenceur_fenetre.jpg "illustrations/4_3_config_georeferenceur_fenetre.jpg")

![Icône effacer un point du géoréférenceur](illustrations/4_3_effacer_point_icone.jpg)Si vous faites une erreur, vous pouvez supprimer un point en cliquant sur l'icône **Effacer un point**, puis sur le point à effacer.

![Icône déplacer un point du géoréférenceur](illustrations/4_3_deplacer_point_icone.jpg)Vous pouvez également déplacer un point déjà créé en cliquant sur l'icône **Deplacer les points de contrôle**, puis en faisant glisser le point à déplacer.

![Icône sauvegarder les points de contrôle](illustrations/4_3_sauv_points_icone.jpg)Une fois vos points créés, vous pouvez les sauvegarder au moyen du menu
 [Fichier → Enregistrer les points de contrôle sous...

![Menu Projet, Fichier, Enregistrer les points de contrôle sous...](illustrations/4_3_sauv_points_menu.jpg)](#thumb "#thumb")
 ou bien en cliquant sur l'icône correspondante.

Cette manipulation crée un fichier avec l'extension .POINTS. Par défaut, ce fichier aura le même nom et sera dans le même dossier que l'image que vous êtes en train de caler. Ces points de calage pourront être chargés dans le géoréférenceur au moyen du **menu Fichier → Charger les points de contrôle...**.

Voici à quoi ressemble la fenêtre du géoréférenceur une fois tous les poins de calage correspondant à des intersections du carroyage renseignés :

[![Cartes de Oahu avec le maximum de points de calage renseignés](illustrations/4_3_avec_tous_les_points.jpg)](illustrations/4_3_avec_tous_les_points.jpg "illustrations/4_3_avec_tous_les_points.jpg")

Vous n'êtes pas obligé de renseigner autant de points ! Six suffiront pour notre calage.

Les points qui serviront à caler notre image sont maintenant créés. Comment faire pour utiliser ces points pour caler notre image ?

[chapitre précédent](04_02_preliminaires.php "04_02_preliminaires.php")
[chapitre suivant](04_04_parametrage.php "04_04_parametrage.php")

[haut de page](#wrap "#wrap")
