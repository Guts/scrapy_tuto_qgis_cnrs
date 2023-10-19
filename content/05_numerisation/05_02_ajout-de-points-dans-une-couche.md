
## V.2 Ajout de points dans une couche

* [Rendre une couche éditable](#V21 "#V21")
* [Ajout d'un point](#V22 "#V22")
* [Modification d'un point](#V23 "#V23")
    * [Déplacement](#V23a "#V23a")
    * [Modification des données attributaires](#V23b "#V23b")
* [Quitter le mode édition](#V24 "#V24")

Nous allons ajouter à la couche créée dans le chapitre précédent les points correspondant aux postes et aux école de la carte de l'île d'Oahu.

Créez un nouveau projet QGIS, et ajoutez-y :

* la carte géoréférencée *[Oahu_Hawaiian_Islands_1906_wgs84.tif](donnees/TutoQGIS_05_Numerisation.zip "donnees/TutoQGIS_05_Numerisation.zip")* située dans le dossier **TutoQGIS_05_Numerisation/donnees**
* la couche vide créée dans le chapitre précédent : *batiments_oahu.shp*

### Rendre une couche éditable

Par défaut, toutes les couches ajoutées dans QGIS sont « verrouillées » donc non modifiables (modifier le style ne modifie pas les données mais seulement leur représentation).

Pour rendre une couche éditable, que ce soit pour modifier les données de la table attributaire ou la géométrie d'un élément, il faut donc passer en mode édition. Nous allons faire cette manipulation pour la couche *batiments_oahu* afin de pouvoir y ajouter des points.

Vérifiez tout d'abord que votre couche de bâtiments soit **au-dessus** de la carte.

Pour passer en mode édition :
 [Clic droit sur le nom de la couche → Basculer en mode édition

![Clic droit sur le nom de la couche, basculer en mode édition](illustrations/5_2_edition_clicdroit.jpg)](#thumb "#thumb")

ou bien :

![icône basculer en mode édition](illustrations/5_2_edition_icone.jpg)sélectionnez la couche dans la table des matières puis cliquez sur l'icône **Basculer en mode édition**

ou encore :

sélectionnez la couche dans la table des matières puis
 [Menu Couche → Basculer en mode édition

![Menu Couche, Basculer en mode édition](illustrations/5_2_edition_menu.jpg)](#thumb "#thumb")
 .

Certains outils de la barre d'outil d'édition deviennent actifs, et dans la table des matières un symbole de crayon apparaît à gauche du nom de la couche :

![symbole de crayon à gauche d'une couche éditable](illustrations/5_2_couche_editable.jpg)
La couche est maintenant modifiable.

Dans QGIS, le passage en mode édition est géré « par couches » : certaines couches peuvent être éditables et d'autres non. Il est facile de voir dans la table des matières quelle couche est éditable.

**De manière générale, il vaut mieux quitter le mode édition dès que vous n'en avez plus besoin, et limiter le nombre de couches éditables.**

Les couches raster ne sont jamais modifiables : si vous sélectionnez la carte de l'île d'Oahu, le passage en mode édition n'est pas possible pour cette couche.

### Ajout d'un point

Commencez par repérer une école ou une poste, représentées respectivement par un point bleu ou rouge, par exemple la poste de la baie de Kaneohe :

[![zoom sur l'école de Kaneohe](illustrations/5_2_ecole_kaneohe.jpg)](illustrations/5_2_ecole_kaneohe.jpg "illustrations/5_2_ecole_kaneohe.jpg")

![icône d'ajout d'une entité ponctuelle](illustrations/5_2_ajout_icone.jpg)Assurez-vous que votre couche de bâtiments soit bien sélectionnée dans la table des matières, puis cliquez sur l'icône **Ajouter une entité ponctuelle**.

Cliquez sur l'école ou la poste que vous avez choisie; une fenêtre s'ouvre vous demandant de renseigner les attributs pour ce point. Laissez **Génération automatique** pour le champ fid, et renseignez le type de bâtiment : **poste**. Cliquez sur **OK**.

Si cette fenêtre ne s'ouvre pas, menu Préférences → Options → rubrique Numérisation : décochez la case « Supprimer la fenêtre de saisie des attributs lors de la création de chaque nouvelle entité » (tout en haut).

[![remplir l'attribut type par 'école' par exemple](illustrations/5_2_remplissage_type.jpg)](illustrations/5_2_remplissage_type.jpg "illustrations/5_2_remplissage_type.jpg")

Le point s'affiche sur la carte, avec le style de la couche (ici un rond turquoise) :

[![point de l'école de Kaneohe](illustrations/5_2_ecole_kaneohe_pt.jpg)](illustrations/5_2_ecole_kaneohe_pt.jpg "illustrations/5_2_ecole_kaneohe_pt.jpg")

Si vous ouvrez la table attributaire de la couche, vous pouvez voir une ligne correspondant au point que vous venez de créer.

Ajoutez d'autres points pour les écoles et postes de l'île.

[![Carte avec toutes les écoles et postes numérisées](illustrations/5_2_tous_les_points.jpg)](illustrations/5_2_tous_les_points.jpg "illustrations/5_2_tous_les_points.jpg")

![icône sauvegarder les modifications](illustrations/5_2_sauv_icone.jpg)N'oubliez pas de sauvegarder vos modifications en sélectionnant la couche puis en cliquant sur l’icône **sauvegarder les modifications**.

Vous pouvez [modifier le style](01_02_info_geo.php#I23a "01_02_info_geo.php#I23a") des points dans les propriétés de la couche, rubrique Symbologie.

Comment faire pour représenter les données comme dans la légende de la carte, les écoles sous forme de rond bleu et les postes de rond rouge ?

![fenêtre des propriétés de la couche, style catégorisé](illustrations/5_2_style_categ.jpg)

Choisissez le style **catégorisé** sur la colonne **type**, cliquez sur **classer** puis double cliquez sur chacun des symboles pour les modifier à votre convenance. Le troisième symbole sera utilisé si certains points ne sont ni des écoles ni des postes. Cliquez sur **OK** pour valider et fermer la fenêtre.

### Modification d'un point

Il peut arriver bien sûr de vouloir modifier un point déjà existant, soit que vous vouliez le déplacer, soit que vous souhaitiez modifier ses données attributaires.

#### Déplacement

Imaginons qu'un de vos points soit mal placé et que vous vouliez le déplacer.

La couche doit être en mode édition.

Il faut également **activer la barre d'outils de numérisation avancée** : clic droit sur n'importe quelle barre d'outils (sauf sur un outil désactivé) et cochez si ça n'est pas déjà le cas la case Barre d'outils de numérisation avancée. Vous pouvez également passer par le menu Vue → Barres d'outils.

![icône déplacer l'entité](illustrations/5_2_deplacer_icone.jpg)Sélectionnez votre couche de bâtiments dans la table des matières, puis cliquez sur l'icône **Déplacer l'entité**.

Le curseur prend la forme d'une croix. Cliquez sur le point à déplacer, puis cliquez sur l'endroit où vous souhaitez déplacer ce point.

#### Modification des données attributaires

Que faire dans le cas où vous voulez modifier les données attributaires d'un point, par exemple le passer de poste à école?

La couche doit être en mode édition.

Ouvrez la table attributaire de la couche.

Double-cliquez sur la case de la table à modifier. Vous pouvez ensuite modifier le texte de cette case.

[![Modification de données attributaires](illustrations/5_2_modif_donnees_attributaires.jpg)](illustrations/5_2_modif_donnees_attributaires.jpg "illustrations/5_2_modif_donnees_attributaires.jpg")

### Quitter le mode édition

Une fois vos ajouts et modifications terminés, il est important de quitter le mode édition, pour plusieurs raisons :

* éviter de faire des modifications par erreur
* sauvegarder les modifications effectuées
* certains outils SIG ne peuvent fonctionner sur une couche en cours d'édition

![icône basculer en mode édition](illustrations/5_2_edition_icone.jpg)Sélectionnez votre couche dans la table des matières et cliquez sur l'icône **basculer en mode édition**.

[![Fenêtre arrêter l'édition](illustrations/5_2_quitter_edition.jpg)](illustrations/5_2_quitter_edition.jpg "illustrations/5_2_quitter_edition.jpg")

Une fenêtre apparaît pour vous demander si vous souhaitez :

* **Fermer sans enregistrer :** quitte le mode édition sans sauvegarder vos modifications
* **Annuler :** ne quitte pas le mode édition
* **Enregistrer :** quitte le mode édition en enregistrant vos modifications.

Cliquez sur **Enregistrer**.

L'icône de crayon à côté de nom de la couche disparaît :

[![nom de la couche, en mode édition (icône crayon) et hors mode édition](illustrations/5_2_quitter_edition_couche.jpg)](illustrations/5_2_quitter_edition_couche.jpg "illustrations/5_2_quitter_edition_couche.jpg")

Le chapitre suivant vous permettra d'en savoir plus sur les modes de saisie des données attributaires, en créant une liste de choix avec les 2 valeurs école et poste.

Vous pouvez bien sûr décider de filer directement au chapitre d'après sur la [numérisation des lignes](05_04_lignes.php "05_04_lignes.php") !

[chapitre précédent](05_01_creation_couche.php "05_01_creation_couche.php")
[chapitre suivant](05_03_donnees_attrib.php "05_03_donnees_attrib.php")

[haut de page](#wrap "#wrap")
