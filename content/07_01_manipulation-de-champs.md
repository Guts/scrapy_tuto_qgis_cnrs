
## VII.1 Manipulation de champs


* [Quels sont les champs présents dans une table ?](#VII11 "#VII11")
* [Créer et supprimer un champ à partir de la table attributaire](#VII12 "#VII12")
	+ [Créer un champ](#VII12a "#VII12a")
	+ [Modifier les valeurs d'un champ manuellement](#VII12b "#VII12b")
	+ [Supprimer un champ existant](#VII12c "#VII12c")
* [Pour aller plus loin : refactoriser les champs](#VII13 "#VII13")




Nous verrons ici comment ajouter et supprimer des champs dans la table attributaire d'une couche existante, et comment modifier l'ordre des champs.


### Quels sont les champs présents dans une table ?



Ouvrez un nouveau projet QGIS, ajoutez la couche *[communes_Bretagne_calcul](donnees/TutoQGIS_07_Champs.zip "donnees/TutoQGIS_07_Champs.zip")*.


Pour voir les champs de la table attributaire de cette couche, vous pouvez bien sûr ouvrir la table attributaire, mais vous pouvez également ouvrir les propriétés de la couche, rubrique **Champs** :



[![fenêtre des propriétés de la couche, rubrique champs](illustrations/7_1_proprietes_champs.jpg)](illustrations/7_1_proprietes_champs.jpg "illustrations/7_1_proprietes_champs.jpg")

Cette fenêtre vous permet de voir d'un seul coup d'œil la liste des champs, leur nom et leur type : **String** (texte), **Integer** (nombre entier) ou **Real** (nombre décimal)...



### Créer et supprimer un champ à partir de la table attributaire


#### Créer un champ


Nous allons ajouter un champs à la couche *communes_Bretagne_calcul*, nommé **NOM_DEPT**, destiné à contenir le nom du département de la commune.



Ouvrez la table attributaire de la couche *communes_Bretagne_calcul*.


![icône passer en mode édition](illustrations/7_1_edition_icone.jpg)[Passez en mode édition](05_02_points.php#V21 "05_02_points.php#V21") pour cette couche.


Cliquez sur l'icône **Ajouter un champ** en haut de la table attributaire :



![barre d'outils de la table attributaire, icône d'ajout de champ entourée en rouge](illustrations/7_1_BO_table_ajout.jpg)

La fenêtre suivante s'ouvre :



[![fenêtre de création de colonne](illustrations/7_1_ajout_fenetre.jpg)](illustrations/7_1_ajout_fenetre.jpg "illustrations/7_1_ajout_fenetre.jpg")

* **Nom :** Tapez **NOM_DEPT**
* **Commentaire :** ce champ peut contenir un commentaire, laissez-le vide
* **Type :** ce champ peut contenir les valeurs suivantes : texte, nombre entier, nombre décimal et date. Choisissez texte puisque nous voulons y mettre les noms des départements
* **Longueur :** Dans le cas d'un champ type texte, cette valeur représente le nombre maximum de caractères que pourra contenir le champ. Tapez 50, ce qui devrait suffire.


Cliquez sur **OK** ; le champ est ajouté à la table, rempli pour l'instant de valeurs nulles.



[![table avec le champ CODE_DEPT vide](illustrations/7_1_table_nouveau_champ.jpg)](illustrations/7_1_table_nouveau_champ.jpg "illustrations/7_1_table_nouveau_champ.jpg")

Quittez le mode édition en enregistrant les modifications.



#### Modifier les valeurs d'un champ manuellement


Il est maintenant possible de taper du texte pour remplir le champ NOM_DEPT que nous venons de créer.



![icône passer en mode édition](illustrations/7_1_edition_icone.jpg)Passez à nouveau en mode édition pour la couche *communes_Bretagne_calcul*.


Ouvrez sa table attributaire si ce n'est pas déjà fait.


Double-cliquez dans une case du champ **NOM_DEPT** :



[![double clic dans une case du champ CODE_DEPT vide](illustrations/7_1_table_modifier.jpg)](illustrations/7_1_table_modifier.jpg "illustrations/7_1_table_modifier.jpg")

Et tapez-y la valeur correspondante (en vous aidant du champ INSEE_DEP qui contient le [code du département](https://fr.wikipedia.org/wiki/Liste_des_d%C3%A9partements_fran%C3%A7ais#Liste_des_d%C3%A9partements "https://fr.wikipedia.org/wiki/Liste_des_d%C3%A9partements_fran%C3%A7ais#Liste_des_d%C3%A9partements")), terminez en appuyant sur la touche entrée :



[![double clic dans une case du champ CODE_DEPT vide](illustrations/7_1_table_modifier_ok.jpg)](illustrations/7_1_table_modifier_ok.jpg "illustrations/7_1_table_modifier_ok.jpg")

Vous pouvez tapez ainsi quelques valeurs.



Vous remarquerez qu'il serait très long de remplir ainsi toutes les lignes de la table. Nous verrons dans le [chapitre suivant](07_02_calculer.php#VII23c "07_02_calculer.php#VII23c") comment remplir automatiquement un champ en fonction des valeurs d'un autre (ici, remplir le nom du département en fonction du code du département).



Quittez le mode édition en enregistrant les modifications.



#### Supprimer un champ existant


Nous allons **supprimer le champ NOM_DEPT** que vous venez de créer (nous créerons un autre champ NOM_DEPT dans le [chapitre suivant](07_02_calculer.php "07_02_calculer.php") que nous remplirons automatiquement).



Passez à nouveau en mode édition pour la couche *communes_Bretagne_calcul*.


Cliquez sur l'icône **Supprimer la colonne** en haut de la table attributaire :



![barre d'outils de la table attributaire, icône de suppression de champ entourée en rouge](illustrations/7_1_BO_table_suppression.jpg)

La fenêtre suivante apparaît :



[![fenêtre de suppression de colonne](illustrations/7_1_suppression_fenetre.jpg)](illustrations/7_1_suppression_fenetre.jpg "illustrations/7_1_suppression_fenetre.jpg")

Sélectionnez le champ **NOM_DEPT** puis cliquez sur **OK**.


Notez qu'il est possible de sélectionner plusieurs champs dans cette fenêtre.


Le champ est supprimé. Quittez le mode édition en enregistrant les modifications.



### Pour aller plus loin : refactoriser les champs


Sous le nom un peu barbare de « refactoriser » se cache la possibilité de **renommer les champs**, ainsi que d'en **modifier l'ordre et le type** (texte, nombre...). Cet outil offre également la possibilité de créer ou supprimer des champs.


Notez que la couche en entrée ne sera pas directement modifiée, une nouvelle couche sera créée.


Nous n'utiliserons pas cet outil, mais vous trouverez ici une brève description de son fonctionnement.


Pour accéder à l'outil : **boîte à outils Traitement → Table vecteur → Refactoriser les champs**.



[![Outil refactoriser dans la boîte à outils Traitement](illustrations/7_1_outil_refactoriser.jpg)](illustrations/7_1_outil_refactoriser.jpg "illustrations/7_1_outil_refactoriser.jpg")


[![Fenêtre de l'outil refactoriser](illustrations/7_1_refactoriser_fenetre.jpg)](illustrations/7_1_refactoriser_fenetre.jpg "illustrations/7_1_refactoriser_fenetre.jpg")

Pour **modifier l'ordre des champs**, sélectionnez un champ en cliquant sur le numéro de sa ligne, puis utilisez les boutons flèche haut et bas à droite de la fenêtre.



Pour **renommer un champ**, double-cliquez sur son nom (colonne Nom du champ) et tapez un nouveau nom. De même, vous pouvez changer son **type**, sa **longueur** et **précision**, et **recalculer ses valeurs** au moyen d'une expression (comme avec la [calculatrice de champ](07_02_calculer.php "07_02_calculer.php")).


Il est également possible **d'ajouter et supprimer un champ**, ainsi que **d'annuler toutes les modifications en cours**.


Dans le chapitre suivant, nous verrons comment calculer automatiquement les valeurs d'un champ au moyen d'une formule, à l'aide de la calculatrice de champ !




[chapitre précédent](07_00_champs.php "07_00_champs.php")
[chapitre suivant](07_02_calculer.php "07_02_calculer.php")


[haut de page](#wrap "#wrap")
