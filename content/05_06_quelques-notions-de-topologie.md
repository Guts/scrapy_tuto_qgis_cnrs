
## V.6 Quelques notions de topologie


* [Qu'est-ce que la topologie ?](#V61 "#V61")
	+ [Définition et exemples](#V61a "#V61a")
	+ [Pourquoi faire attention à la topologie ?](#V61b "#V61b")
* [Pour aller plus loin : comment vérifier la topologie d'une couche ?](#V62 "#V62")
	+ [Vérification simple](#V62a "#V62a")
	+ [Utilisation du vérificateur de topologie](#V62b "#V62b")
* [Corriger les erreurs de topologie : quelques pistes](#V63 "#V63")
	+ [Corriger les erreurs de topologie manuellement](#V63a "#V63a")
	+ [Corriger les erreurs de topologie avec l'outil «  réparer les géométries »](#V63b "#V63b")
	+ [Corriger les erreurs de topologie avec l'outil v.clean de Grass](#V63c "#V63c")
	+ [Cas particulier des erreurs de type « auto-intersection »](#V63d "#V63d")




Au cours de la dernière partie notamment, nous avons vu comment éviter que deux polygones soient « presque » jointifs, au moyen de propriétés telles que l'accrochage, ou par l'utilisation d'outils de découpage par exemple. Nous avons également vu comment utiliser le mode d'édition topologique de QGIS.


Nous allons ici en apprendre un peu plus sur ce qu'est la topologie, et comment vérifier la topologie d'une couche.


### Qu'est-ce que la topologie ?


#### Définition et exemples


La [topologie](http://www.cnrtl.fr/definition/topologie "http://www.cnrtl.fr/definition/topologie") est la « partie de la géométrie qui considère uniquement les relations de position » (Aur.-Weil 1981).


En géomatique, la topologie est utilisée pour décrire les relations entre les géométries des entités. Des règles de topologie peuvent être définies, et les erreurs de topologie détectées.


Par exemple, on peut décider qu'il ne doit y avoir aucune superposition de polygones dans une couche (les erreurs sont en rouge) :



[![deux polygones se superposant en partie](illustrations/5_6_overlap.jpg)](illustrations/5_6_overlap.jpg "illustrations/5_6_overlap.jpg")

Ou bien qu'il ne doit pas y avoir de trous entre les polygones :



[![deux polygones avec un trou entre les deux](illustrations/5_6_gap.jpg)](illustrations/5_6_gap.jpg "illustrations/5_6_gap.jpg")

Les règles de topologie peuvent aussi mettre en jeu plusieurs couches. Par exemple, tous les points d'une couche doivent être dans un polygone d'une autre couche :



[![des points dans des polygones sauf deux](illustrations/5_6_pts_dans_polygones.jpg)](illustrations/5_6_pts_dans_polygones.jpg "illustrations/5_6_pts_dans_polygones.jpg")

Il est bien sûr possible de combiner plusieurs règles. Vous trouverez dans le [manuel de QGIS](https://docs.qgis.org/testing/en/docs/gentle_gis_introduction/topology.html "https://docs.qgis.org/testing/en/docs/gentle_gis_introduction/topology.html") la description d'un certain nombre de règles de topologie.


#### Pourquoi faire attention à la topologie ?


Ne pas respecter les règles de topologie peut poser des problèmes lors de l'utilisation d'outils d'analyse spatiale, qui donneront alors des résultats inattendus.


### Pour aller plus loin : comment vérifier la topologie d'une couche ?


Cette partie est pour « aller un peu plus loin » : vous pouvez donc passer directement à la partie suivante si vous le désirez !


Sinon, vous aurez besoin d'un projet QGIS avec une couche de polygones, par exemple *zones_oahu*.


#### Vérification simple



Vérifiez d'abord que votre couche de polygones *zones_oahu* n'est pas en mode édition.


Pour vérifier rapidement la topologie d'une couche, utilisez l'outil **Vérifier la validité**, accessible dans la boîte à outils (en tapant *valid* dans la barre de recherche par exemple) :



[![accéder à l'outil vérifier la validité dans la toolbox](illustrations/5_6_verif_toolbox.jpg)](illustrations/5_6_verif_toolbox.jpg "illustrations/5_6_verif_toolbox.jpg")

Si la boîte à outils n'est pas visible, allez dans le menu Traitement → Boîte à outils.



[![fenêtre de validation de la géométrie](illustrations/5_6_verif_fenetre.jpg)](illustrations/5_6_verif_fenetre.jpg "illustrations/5_6_verif_fenetre.jpg")

Sélectionnez la couche *zones_oahu* et cliquez sur **Exécuter**.


3 couches temporaires sont ajoutées au projet :


* **sortie valide** liste les entités valide
* **sortie invalide** liste les entités invalides (avec une ou plusieurs erreurs de topologie
* **erreur de sortie** liste les erreurs de topologie rencontrées, un point par erreur.


Si vous n'avez pas d'erreur de topologie dans votre couche, la couche **sortie valide** contiendra autant d'entités que la couche d'origine, et les couches **sortie invalide** et **erreur de sortie** n'en contiendront aucune.



#### Utilisation du vérificateur de topologie


Le **vérificateur de topologie** est un outil plus perfectionné qui permet de spécifier un certain nombre de règles, et de voir les erreurs relatives à ces règles. Il s'agit d'une extension principale, qui ne peut pas être désinstallée.



Il faut tout d'abord vérifier que cette extension soit activée.


Pour cela, rendez-vous dans le **menu Extensions → Installer/Gérer les extensions**. Dans la rubrique **Installées**, vérifiez que la case du **Vérificateur de topologie** soit bien cochée, et cochez-la si ça n'est pas le cas :



[![Gestionnaire d'extensions, rubrique 'Installées', avec la ligne du vérificateur de topologie surlignée en rouge, la case est cochée](illustrations/5_6_veriftopo_activation.jpg)](illustrations/5_6_veriftopo_activation.jpg "illustrations/5_6_veriftopo_activation.jpg")

Vous pouvez maintenant accéder au vérificateur de topologie :
 [menu Vecteur → Vérificateur de topologie

![Menu Vecteur, Vérificateur de topologie](illustrations/5_6_veriftopo_menu.jpg)](#thumb "#thumb")
 :



[![fenêtre (intégrée) du vérificateur de topologie](illustrations/5_6_veriftopo_fenetre.jpg)](illustrations/5_6_veriftopo_fenetre.jpg "illustrations/5_6_veriftopo_fenetre.jpg")

Cliquez sur le bouton **Configuration** pour ajouter ou supprimer des règles de topologie. Nous allons ajouter une règle pour interdire les superpositions de polygones dans la couche *zones_oahu*.



[![fenêtre de gestion des règles de topologie](illustrations/5_6_regle_fenetre.jpg)](illustrations/5_6_regle_fenetre.jpg "illustrations/5_6_regle_fenetre.jpg")

Sélectionnez la couche **zones_oahu** dans la liste déroulante, puis la propriété **ne doit pas se superposer** et cliquez enfin sur le bouton **Ajouter une règle**. Cliquez sur **OK**.


Pour visualiser les erreurs à cette règle, cliquez sur le bouton **Valider tout** du vérificateur de topologie.



[![fenêtre du vérificateur de topologie, pas d'erreurs](illustrations/5_6_veriftopo_erreurs.jpg)](illustrations/5_6_veriftopo_erreurs.jpg "illustrations/5_6_veriftopo_erreurs.jpg")

La liste des éventuelles erreurs apparaît ; il est possible de zoomer sur une erreur en double-cliquant sur la ligne correspondante.



### Corriger les erreurs de topologie : quelques pistes


Cette partie n'est pas très étoffée et mériterait un chapitre à part entière ! A venir ?


#### Corriger les erreurs de topologie manuellement


Pour corriger les erreurs de topologie d'une couche, vous pouvez procéder « à la main », en corrigeant les erreurs une à une avec les outils d'édition de QGIS, en utilisant les **propriétés d'accrochage** et l'**outil de noeud**. Cliquer sur la ligne correspondant à une erreur dans le vérificateur de topologie zoome sur cette erreur.


#### Corriger les erreurs de topologie avec l'outil «  réparer les géométries »


Il existe un outil **Réparer les géométries** accessible dans la boîte à outils de traitement. Pour afficher (ou masquer si elle est déjà affichée) cette boîte, **menu Traitement → Boîte à outils**. Tapez ensuite **réparer** dans la partie filtre pour trouver facilement cet outil :



[![accès à l'outil réparer les géométries à partir de la boîte à outils](illustrations/5_6_reparer.jpg)](illustrations/5_6_reparer.jpg "illustrations/5_6_reparer.jpg")

Cet outil prend une couche en entrée (la couche contenant des erreurs) et génère une nouvelle couche, normalement sans erreurs de topologie, en sortie.


#### Corriger les erreurs de topologie avec l'outil v.clean de Grass


Vous pouvez également utiliser l'outil **v.clean** issu de **Grass**, toujours dans la boîte à outils de traitements. Tapez **clean** dans le filtre pour accéder à l'outil **v.clean**.



[![accès à l'outil vclean à partir de la boîte à outils](illustrations/5_6_vclean.jpg)](illustrations/5_6_vclean.jpg "illustrations/5_6_vclean.jpg")

En double-cliquant sur cet outil, une aide est accessible dans l'onglet Help, ou bien ici : [https://grass.osgeo.org/grass70/manuals/v.clean.html](https://grass.osgeo.org/grass70/manuals/v.clean.html "https://grass.osgeo.org/grass70/manuals/v.clean.html"). Regardez également [ici](http://grasswiki.osgeo.org/wiki/Vector_topology_cleaning "http://grasswiki.osgeo.org/wiki/Vector_topology_cleaning") pour plus de documentation.


#### Cas particulier des erreurs de type « auto-intersection »


Vous rencontrerez peut-être des erreurs de topologie de type « self-intersection » dans une couche de polygones : ces erreurs peuvent généralement être réparées en créant une [zone tampon](09_01_vecteur.php#VIII23b "09_01_vecteur.php#VIII23b") de 0 autour de la couche originale.




[chapitre précédent](05_05_polygones.php "05_05_polygones.php")
[partie VI : requêtes](06_00_requetes.php "06_00_requetes.php")


[haut de page](#wrap "#wrap")
