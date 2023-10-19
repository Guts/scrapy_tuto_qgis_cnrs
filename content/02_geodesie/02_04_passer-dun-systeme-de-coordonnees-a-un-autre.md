
## II.4 Passer d'un système de coordonnées à un autre

* [Modifier le SCR du projet](#II41 "#II41")
* [Modifier le SCR d'une couche](#II42 "#II42")
* [Redéfinir le SCR d'une couche](#II43 "#II43")
* [Modifier et redéfinir le SCR : à ne pas confondre !](#II44 "#II44")

### Modifier le SCR du projet

Vous avez pu constater dans la partie [II.3 Couches et projets : à chacun son système](02_03_couches_projets.php "02_03_couches_projets.php") que les couches d'un projet sont affichées dans le SCR du projet. Comment modifier le SCR du projet pour afficher les couches dans le SCR de votre choix ?

Nous allons modifier le SCR du projet *monde.qgz* du WGS84 vers [Robinson](http://fr.wikipedia.org/wiki/Projection_de_Robinson "http://fr.wikipedia.org/wiki/Projection_de_Robinson") (code EPSG 53030).

![Icône Ouvrir](illustrations/1_4_ouvrir_projet_icone.jpg)A partir de QGIS, ouvrez le projet *[monde.qgz](donnees/TutoQGIS_02_Geodesie.zip "donnees/TutoQGIS_02_Geodesie.zip")* situé dans le dossier **TutoQGIS_02_Geodesie/projets**

(Si vous avez déjà un autre projet du tutoriel ouvert, il est inutile de le sauvegarder).

Ce projet comporte une couche de pays, une couche avec les [indicatrices de Tissot](02_02_coord.php#II22c "02_02_coord.php#II22c"), et une couche de graticule, c'est-à-dire de méridiens et de parallèles distants ici de 15 degrés.

Dans quel SCR sont les 3 couches du projet ?

Elles sont toutes les 3 en WGS84, code EPSG 4326 (pour le vérifier, allez dans les propriétés de la couche, rubrique Information).

[Ouvrez les propriétés du projet

![Menu Projet, Propriétés du projet](illustrations/2_3_proprietes_projet_menu.jpg)](#thumb "#thumb")
 , rubrique SCR :

[![Modifier le SCR d'un projet](illustrations/2_4_modif_scr_projet.jpg)](illustrations/2_4_modif_scr_projet.jpg "illustrations/2_4_modif_scr_projet.jpg")

*1.* Vérifiez que la case **Aucun SCR** soit bien décochée.

*2.* Tapez **robinson** dans cette partie, ou bien 53030 (code EPSG).

*3.* Le filtre est activé dans la liste des derniers SCR utilisés. Selon si vous avez déjà utilisé Robinson ou non, cette partie sera donc ou vide ou avec une ou deux lignes correspondant à ce système.

*4.* Le filtre est également activé dans la liste de tous les SCR disponibles : seuls les SCR dont le nom contient "Robinson" sont affichés. **Sélectionnez Sphere Robinson, code EPSG 53030**.

*5.* **Vous devez voir dans cette partie le SCR que vous venez de sélectionner.**

Cliquez sur **OK**.

Toutes les couches du projet sont désormais affichées en Robinson. Leur SCR n'a cependant pas été modifié, ce que vous pouvez [vérifier](02_03_couches_projets.php#II32 "02_03_couches_projets.php#II32"). Observez les modifications apportées aux pays et aux indicatrices de Tissot.

Si des bugs d'affichage apparaissent, zoomez ou dézoomez.

Répétez cette manipulation pour que le SCR du projet passe en :

* Mercator, code EPSG 54004
* Projection azimutale équidistante du pôle Sud, code EPSG 102019
* RGF93 / Lambert-93, code EPSG 2154

Qu'observez-vous dans ce dernier cas ? A quoi cela est-il dû ?

Le RGF93 / Lambert-93 est un système adapté à l'emprise de la France métropolitaine ; tout le reste du monde est donc de plus en plus déformé au fur et à mesure qu'on s'éloigne de la France.

Nous allons maintenant repasser le projet en WGS84. Puisqu'il existe dans ce projet des couches en WGS84, vous pouvez utiliser un raccourci pour cela :

[Clic-droit sur une couche (n'importe laquelle puisqu'elles sont toutes trois en WGS84) → SCR de la couche → Définir le SCR du projet depuis cette couche

![Définir le SCR du projet à partir du SCR d'une couche](illustrations/2_4_def_scr_projet_couche.jpg)](#thumb "#thumb")

Le SCR du projet est maintenant le même que celui de la couche, c'est-à-dire WGS84.

Vous avez pu constater que modifier le SCR du projet ne modifie pas les données. Cette manipulation permet de visualiser les données dans le SCR de votre choix, à des fins cartographiques par exemple.

### Modifier le SCR d'une couche

Nous avons vu que QGIS gère le cas où plusieurs couches dans différents SCR sont affichés dans un même projet. Cependant, certaines manipulations nécessitent que toutes les couches soient dans le même SCR. Par ailleurs, par souci de clarté et pour éviter les erreurs, on peut vouloir travailler avec des couches dans le même SCR.

Pour toutes ces raisons, il est utile de savoir modifier le SCR d'une couche.

Cette manipulation implique de **recalculer les coordonnées de tous les objets de la couche dans un autre SCR**.

Par exemple, si la couche d'origine est en WGS84 et contient un point correspondant à la ville de Paris, et que le but est d'obtenir une couche en RGF93 / Lambert-93 , les coordonnées initiales du point (48,89 2,35) en WGS84 seront recalculées pour devenir (652381 6862047) en RGF93 / Lambert-93.

Cette manipulation **crée une nouvelle couche**. La couche d'origine et la couche résultat se superposeront exactement dans QGIS, puisqu'elles contiendront exactement les mêmes objets.

L'objectif sera ici de créer une nouvelle couche pays dans la projection de Bonne (code ESRI 53024).

Pour cela, affichez la **boîte à outils de traitements** : menu Traitements → Boîte à outils.

[![Emplacement de l'outil reprojeter dans la boîte à outils de traitements](illustrations/2_4_traitement_reprojeter.jpg)](illustrations/2_4_traitement_reprojeter.jpg "illustrations/2_4_traitement_reprojeter.jpg")

Dans la barre de recherche de cette boîte à outils, tapez **projection** et double-cliquez sur l'outil **Reprojeter une couche**.

Vous noterez que cet outil est improprement nommé : il peut en effet être utiliser pour modifier le SCR d'une couche, que les SCR de départ et d'arrivée soit projetés ou géographiques !

La fenêtre suivante apparaît :

[![Fenêtre de l'outil reprojeter](illustrations/2_4_reprojeter_fenetre.jpg)](illustrations/2_4_reprojeter_fenetre.jpg "illustrations/2_4_reprojeter_fenetre.jpg")

* Couche source : sélectionnez **ne_110m_admin_0_countries** dans la liste
* SCR cible : cliquez sur l'icône à droite et choisissez le SCR **Sphere Bonne, code ESRI 53024**
* Advanced Parameters : dans certains cas, pour passer d'un SCR à un autre, différentes transformations sont disponibles. Nous n'utiliserons pas ici cette option
* Reprojeté : laissez l'option par défaut, à savoir créer une couche temporaire. Le but étant ici de tester la manipulation, il n'est pas nécessaire de sauvegarder une nouvelle couche sur votre ordinateur.

Cliquez sur **Exécuter**.

Si vous avez bien coché la case correspondante, la couche est automatiquement ajoutée à la carte. Sinon, ajoutez-la dans QGIS.

Vérifiez dans ses propriétés que son SCR soit bien Sphere Bonne.

Comment afficher cette couche dans son SCR, pour savoir à quoi ressemble la projection de Bonne ?

Clic droit sur le nom de la couche → SCR de la couche → Définir le SCR du projet depuis cette couche, ou bien dans les propriétés du projet, rubrique SCR, choisissez le SCR Sphere Bonne.

[![Projection de Bonne](illustrations/2_4_bonne.jpg)](illustrations/2_4_bonne.jpg "illustrations/2_4_bonne.jpg")

Modifier le SCR d'une couche crée une nouvelle couche. Cette manipulation est utile pour pouvoir effectuer ensuite des traitements sur les données, ou pour éviter toute source de confusion en ayant uniquement des données dans le même SCR.

### Redéfinir le SCR d'une couche

Il existe une autre manipulation souvent confondue avec le fait de modifier le SCR d'une couche : **redéfinir le SCR d'une couche**. Dans ce cas, les coordonnées ne sont pas recalculées et aucune nouvelle couche n'est créée, le SCR associé à la couche est simplement modifié.

Pour reprendre l'exemple utilisé plus haut d'une couche en WGS84 contenant un point correspondant à la ville de Paris de coordonnées (48,89 2,35), si le SCR de cette couche est redéfini en RGF93 / Lambert-93, les coordonnées du point resteront (48,89 2,35) mais ces coordonnées seront renseignées comme étant mesurées dans le SCR RGF93 / Lambert-93.

Le point ne sera donc pas affiché, ou affiché à un endroit aberrant, puisqu'il n'est pas possible de trouver de telles coordonnées dans ce SCR (en RGF93 / Lambert-93, les X varient de 100 000 à 1 200 000 et les Y de 6 000 000 à 7 100 000).

Redéfinir le SCR d'une couche n'est donc utile que dans deux cas bien précis :

* **le SCR n'est pas défini du tout**, ce qui peut arriver par exemple pour certaine couches trouvées sur internet. Il faudra alors retrouver dans quel SCR a été initialement créée la couche
* **le SCR est mal défini** (quelqu'un - ou vous-même ! - a donc déjà effectué cette manipulation à tort)

Si ça n'est pas clair, une autre [tentative d'explication plus bas](#II44 "#II44")&nbsp!

Pour être sûr de vous rendre compte si une couche n'a pas de SCR défini, rendez-vous dans le menu
 [Préférences → Options

![Menu Préférences, Options](illustrations/2_3_preferences_options_menu.jpg)](#thumb "#thumb")
 , rubrique **SCR** :

[![Options, rubrique SCR](illustrations/2_4_options_sans_scr.jpg)](illustrations/2_4_options_sans_scr.jpg "illustrations/2_4_options_sans_scr.jpg")

Pour l'option **Quand une nouvelle couche est créée ou quand une couche est chargée sans SCR**, choisissez l'option **Demander le SCR**.

Ainsi, si vous chargez une couche dont le SCR n'est pas défini, QGIS vous avertira et vous demandera de spécifier un SCR pour cette couche (ce sera cependant à vous de retrouver le SCR initial dans lequel aura été créée cette couche).

Nos couches ayant un SCR correctement défini, cette manip ne nous est pas utile ici, mais pour info, voici comment procéder :

* Pour redéfinir **temporairement** le SCR d'une couche : propriétés de la couche → rubrique Source (utile pour tester et retrouver le bon SCR)
* Pour redéfinir le SCR d'une couche de manière permanente (crée une nouvelle couche) : boîte à outils → Assigner une projection
* Idem que ci-dessus mais ne crée pas de nouvelle couche, uniquement pour les shapefiles : boîte à outils → Définir la projection du fichier shapefile

### Modifier et redéfinir le SCR : à ne pas confondre !

La confusion entre les 2 manipulations **modifier le SCR** (outil reprojeter) et **(re)définir le SCR** (dans les propriétés de la couche) est une source d'erreur très courante !

Pour y voir clair, on peut prendre l'analogie d'un livre. Sur ce livre est collée une étiquette indiquant qu'il est en français. Si vous voulez traduire ce livre en anglais, vous allez traduire tout le contenu du livre (recalculer les coordonnées dans le nouveau SCR), puis enlever l'étiquette « français » pour coller à la place une étiquette « anglais » ; c'est l'équivalent de l'opération consistant à modifier le SCR.

Redéfinir le SCR consisterait à enlever l'étiquette « français » pour coller à la place une étiquette « anglais »  **sans traduire le contenu du livre** (pas de recalcul des coordonnées). On aurait donc un livre toujours en français, mais mal étiqueté.

Redéfinir le SCR (changer l'étiquette) n'est donc utile que si l'étiquette n'était pas la bonne, ou bien qu'il n'y avait pas d'étiquette du tout (SCR mal défini ou non défini).

Autrement dit :

[![Analogie d'un livre à traduire pour expliquer la différence entre modifier et redéfinir le SCR](illustrations/2_4_ne_pas_confondre.png)](illustrations/2_4_ne_pas_confondre.png "illustrations/2_4_ne_pas_confondre.png")

[chapitre précédent](02_03_couches_projets.php "02_03_couches_projets.php")
[partie III : recherche et ajout de données](03_00_recherche_ajout.php "03_00_recherche_ajout.php")

[haut de page](#wrap "#wrap")
