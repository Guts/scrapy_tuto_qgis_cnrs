
## IV.6 Points de calage : en se basant sur une couche de référence


* [Ajout d'un fonds OpenStreetMap](#IV61 "#IV61")
* [Zoom sur la zone d'étude avec l'extension Nominatim Locator Filter](#IV62 "#IV62")
* [Création des points de calage](#IV63 "#IV63")




Comme expliqué dans la [partie IV.1.2](04_01_principe.php#IV12 "04_01_principe.php#IV12"), il est également possible de se baser sur une couche de référence pour géoréférencer une image.


La manipulation sera la même que décrite dans les précédentes parties, sauf en ce qui concerne la création des points de calage. Seule cette partie sera donc décrite ici.


L'image que nous allons caler est une carte de Doncaster East, dans la banlieue de Melbourne (source : [Wikimedia](http://commons.wikimedia.org/wiki/File:Doncaster_east_locality_map.PNG "http://commons.wikimedia.org/wiki/File:Doncaster_east_locality_map.PNG")).



[![Carte à caler de Doncaster East (Australie)](illustrations/4_6_doncaster_east.jpg)](illustrations/4_6_doncaster_east.jpg "illustrations/4_6_doncaster_east.jpg")

Pour caler cette carte, nous allons nous baser sur les données [OpenStreetMap](http://www.openstreetmap.org/ "http://www.openstreetmap.org/"). OpenStreetMap est une base de données cartographique libre ; on décrit souvent ce projet comme un "wikipedia cartographique". Pour en savoir plus, voir aussi [ici](03_05_donnees_osm.php "03_05_donnees_osm.php") !


### Ajout d'un fonds OpenStreetMap


2 méthodes permettant d'afficher un fonds OpenStreetMap sont décrites [ici](03_04_fonds_carte.php "03_04_fonds_carte.php").



Vous pouvez par exemple vous rendre dans le panneau Explorateur (s'il n'est pas déjà activé : menu Vue → Panneaux → Explorateur), rubrique **XYZ Tiles**, et double-cliquez sur le fonds **OpenStreetMap**.



[![Panneau Explorateur, XYZ Tiles, OpenStreetMap](illustrations/4_6_ajout_OSM.jpg)](illustrations/4_6_ajout_OSM.jpg "illustrations/4_6_ajout_OSM.jpg")



Dans quel système de coordonnées est la couche OSM ?


Le [SCR de le couche](02_03_couches_projets.php#II32 "02_03_couches_projets.php#II32") est le WGS84 projection Pseudo Mercator, EPSG:3857.



La couche ajoutée est projetée à la volée dans le SCR du projet.


Pour simplifier les choses, nous allons passer le projet également en Pseudo Mercator, afin que la couche de base pour le géoréférencement et le projet aient le même SCR.


Pour cela, rendez-vous dans les propriétés du projet et sélectionnez le SCR Pseudo Mercator, code EPSG 3857 (cf. [ici](02_04_changer_systeme.php#II41 "02_04_changer_systeme.php#II41")). Vous devez maintenant voir le SCR 3857 dans la barre en bas de la fenêtre de QGIS :



[![SCR du projet lisible dans la barre du bas de la fenêtre de QGIS (ici EPSG:3857)](illustrations/4_6_scr_projet_3857.jpg)](illustrations/4_6_scr_projet_3857.jpg "illustrations/4_6_scr_projet_3857.jpg")


### Zoom sur la zone d'étude avec l'extension Nominatim Locator Filter


Nous cherchons ici à zoomer sur la zone qui concerne notre carte, à savoir Doncaster East dans le banlieue de Melbourne, en Australie. Il est bien sûr possible d'utiliser les outils de zoom pour cela, mais nous allons en profiter pour découvrir une autre méthode parfois bien pratique, avec l'extension [Nominatim Locator Filter](https://github.com/rduivenvoorde/nominatim_locator_filter "https://github.com/rduivenvoorde/nominatim_locator_filter").



Commençons par installer l'extension **Nominatim Locator Filter** : procédez comme pour QuickMapServices, via le **menu Extensions → Installer/Gérer les extensions**.



[![Installation de l'extension Nominatim Locator Filter](illustrations/4_6_install_nlf.jpg)](illustrations/4_6_install_nlf.jpg "illustrations/4_6_install_nlf.jpg")

L'extension n'est pas visible dans QGIS ; en fait, cette extension ajoute une fonctionnalité à la barre de recherche tout en bas à gauche de la fenêtre de QGIS.



[![Fenêtre de QGIS avec la barre de recherche en bas à gauche encadrée en rouge](illustrations/4_6_barre_recherche.jpg)](illustrations/4_6_barre_recherche.jpg "illustrations/4_6_barre_recherche.jpg")


Cette barre de recherche permet de rechercher une couche chargée dans le projet, un algorithme de traitement... L'extension Nominatim Locator Filter lui ajoute la fonctionnalité permettant de rechercher des noms de lieux dans OpenStreetMap et de zoomer sur la zone correspondante (qu'une couche OSM soit chargée dans le projet en cours ou non).


**Pour cela, il faut taper le nom du lieu à rechercher puis le caractère espace.**



Dans la barre de recherche, tapez : **Doncaster East, Victoria, Australia**  en terminant par un espace.


Appuyez sur la touche entrée pour valider la suggestion qui doit normalement apparaître : la carte est maintenant zoomée sur ce lieu.



[![Données OSM : Melbourne](illustrations/4_6_osm_zoom1.jpg)](illustrations/4_6_osm_zoom1.jpg "illustrations/4_6_osm_zoom1.jpg")



Zoomez maintenant sur Doncaster East (pour vous aider : [carte OpenStreetMap de Doncaster Est](http://www.openstreetmap.org/relation/2390038#map=13/-37.7776/145.1615 "http://www.openstreetmap.org/relation/2390038#map=13/-37.7776/145.1615")).



[![Doncaster East : données OSM et carte à caler en vis à vis](illustrations/4_6_osm_doncaster_east.jpg)](illustrations/4_6_osm_doncaster_east.jpg "illustrations/4_6_osm_doncaster_east.jpg")


Savez-vous qu'il existe une version française de cette extension, [French locator Filter](https://github.com/Oslandia/french_locator_filter "https://github.com/Oslandia/french_locator_filter"), basée sur l'API publique [https://geo.api.gouv.fr/adresse](https://geo.api.gouv.fr/adresse "https://geo.api.gouv.fr/adresse") ?


Nous allons maintenant pouvoir procéder à la création des points de calage.


### Création des points de calage



Ouvrez la fenêtre du géoréférenceur et ajoutez l'image à caler : *[Doncaster_east_locality_map.PNG](donnees/TutoQGIS_04_Georef.zip "donnees/TutoQGIS_04_Georef.zip")* située dans le dossier **TutoQGIS_04_Georef/donnees** (si nécessaire, aidez-vous pour cela du début de la [partie IV.3.1](04_03_calage_carroyage.php#IV31 "04_03_calage_carroyage.php#IV31")).


Si QGIS vous demande dans quel SCR est cette image, choisissez le **WGS84 / Pseudo-Mercator EPSG:3857**.


Cliquez sur une intersection de routes, par exemple entre Reynolds Road et Blackburn Road. La fenêtre de saisie des coordonnées apparaît : cliquez sur le bouton **Depuis le canevas de la carte**.



[![fenêtre de saisie des coordonnées](illustrations/4_6_depuis_canevas.jpg)](illustrations/4_6_depuis_canevas.jpg "illustrations/4_6_depuis_canevas.jpg")

Dans la fenêtre de QGIS, cliquez sur cette intersection sur les données OSM : les coordonnées de la fenêtre de saisie sont automatiquement remplies avec les coordonnées du point sur lequel vous venez de cliquer.



[![les coordonnées sont remplies en fonction du point cliqué dans QGIS](illustrations/4_6_coord_remplies.jpg)](illustrations/4_6_coord_remplies.jpg "illustrations/4_6_coord_remplies.jpg")

Notez également que le SCR du projet est automatiquement sélectionné !


Cliquez sur **OK**.



[![point 0, dans la fenêtre du géoréférenceur et dans celle de QGIS](illustrations/4_6_point_0.jpg)](illustrations/4_6_point_0.jpg "illustrations/4_6_point_0.jpg")
Premier point : à gauche, dans la fenêtre de QGIS (données OSM) et à droite, dans la fenêtre du géoréférenceur.

Procédez de la même manière pour obtenir au moins six points de calage.


Si vous avez besoin de **vous déplacer dans la fenêtre de QGIS avant de cliquer pour créer le point** : vous pouvez laisser la **barre d'espace** appuyée en bougeant la souris, et zoomer et dézoomer avec la molette. Vous pouvez aussi sélectionner l'outil **Se déplacer dans la carte** (icône de main) ; dans ce cas, revenez ensuite à la fenêtre du géoréférenceur et cliquez à nouveau sur le bouton **Depuis le canevas de la carte** pour créer le point.


Ensuite, choisissez les [paramètres du géoréférencement](04_04_parametrage.php "04_04_parametrage.php") : vous pouvez choisir les mêmes que précédemment, mais **n'oubliez pas de sélectionner le SCR WGS84 Pseudo-Mercator EPSG:3857 au lieu du WGS84 EPSG:4326**.


[Lancez le calage](04_05_lancement.php "04_05_lancement.php").


Une fois le calage terminé, vous pouvez en vérifier la précision en donnant de la transparence à votre image calée (dans les propriétés de la couche, rubrique Transparence) :



[![Superposition de l'image calée et des données OSM](illustrations/4_6_superposition.jpg)](illustrations/4_6_superposition.jpg "illustrations/4_6_superposition.jpg")


L'image est calée, son SCR est WGS84 Pseudo-Mercator (vous pouvez le vérifier en allant dans les propriétés de la couche, rubrique Général). Si vous désirez modifier le SCR de cette couche, comme indiqué dans la [partie II.4.2](02_04_changer_systeme.php#II42 "02_04_changer_systeme.php#II42"), utilisez l'outil **Reprojeter une couche**.




[chapitre précédent](04_05_lancement.php "04_05_lancement.php")
[partie V : numérisation](05_00_numerisation.php "05_00_numerisation.php")


[haut de page](#wrap "#wrap")
