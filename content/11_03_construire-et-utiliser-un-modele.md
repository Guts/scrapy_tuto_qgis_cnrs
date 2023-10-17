
## XI.3 Construire et utiliser un modèle

* [Création d'un modèle](#XI31 "#XI31")
    * [Création du premier paramètre en entrée : couche à découper](#XI31a "#XI31a")
    * [Création du deuxième paramètre en entrée : masque de découpe](#XI31b "#XI31b")
    * [Création du premier algorithme : découpage](#XI31c "#XI31c")
    * [Création du second algorithme : modification du SCR](#XI31d "#XI31d")
* [Enregistrement et documentation d'un modèle](#XI32 "#XI32")
    * [Enregistrer un modèle](#XI32a "#XI32a")
    * [Documenter un modèle](#XI32b "#XI32b")
* [Application](#XI33 "#XI33")
    * [Découpage et reprojection d'une couche](#XI33a "#XI33a")
    * [Découpage et reprojection de plusieurs couches (utilisation « par lot »)](#XI33b "#XI33b")

Les modèles sont surtout utiles pour chaîner plusieurs traitements. Par exemple, imaginons que notre but soit non seulement de découper une couche par une autre, mais ensuite de changer le SCR de la couche découpée pour la passer en WGS84 par exemple.

Il est possible de **créer un modèle enchaînant les deux outils**, qui pourra être lancé facilement sur plusieurs couches, et même être exécuté [par lot](11_02_par_lot.php "11_02_par_lot.php").

Dans la boîte à outils Traitements, cliquez sur l'icône **Modèles** tout en haut à gauche et choisissez **Créer un nouveau modèle**.

[![Emplacement de l'outil de création de modèles dans la boîte à outils Traitements](illustrations/11_03_creer_modele.jpg)](illustrations/11_03_creer_modele.jpg "illustrations/11_03_creer_modele.jpg")

La fenêtre qui s'ouvre comporte une partie à gauche avec 2 onglets, Entrées et Algorithmes, qui vont vous servir à créer le modèle, et une partie vide à droite où votre modèle sera représenté.

Notre modèle comportera 2 paramètres en entrée : une couche vecteur qui sera découpée et une couche vecteur qui servira de masque de découpe. L'outil de découpage va utiliser ces deux paramètres en entrée pour créer une nouvelle couche temporaire. Cette couche temporaire sera utilisée comme paramètre d'entrée pour l'outil de reprojection, qui produira la couche finale.

[![Organigramme du modèle qui sera créé](illustrations/11_03_organigramme.svg)](illustrations/11_03_organigramme.svg "illustrations/11_03_organigramme.svg")

### Création d'un modèle

#### Création du premier paramètre en entrée : couche à découper

Dans l'onglet **Entrées** dans la partie gauche de la fenêtre, double-cliquez sur **Couche vecteur** :

[![Fenêtre du modeleur de traitement](illustrations/11_03_modeleur_fenetre.jpg)](illustrations/11_03_modeleur_fenetre.jpg "illustrations/11_03_modeleur_fenetre.jpg")

[![Fenêtre de définition d'un paramètre](illustrations/11_03_def_parametre_fenetre.jpg)](illustrations/11_03_def_parametre_fenetre.jpg "illustrations/11_03_def_parametre_fenetre.jpg")

* Nom du paramètre : **couche à découper**
* Type de géométrie : **Tout type de géométrie**, puisque cette couche peut aussi bien être de type point, ligne ou polygone
* **Obligatoire** : cochez la case, il ne s'agit pas d'un paramètre optionnel

Le paramètre est ajouté au modèle sous forme d'une boîte verte. Vous pouvez éditer ses caractéristiques en double-cliquant sur cette boîte, ou bien en cliquant sur les poinst de suspension en bas à droite de la boîte.

[![Boîte pour la couche source](illustrations/11_03_modele_01.jpg)](illustrations/11_03_modele_01.jpg "illustrations/11_03_modele_01.jpg")

![icône zoom complet](illustrations/11_03_zoom_icone.jpg)Si à un moment donné vous ne voyez plus votre modèle dans la partie droite de la fenêtre, cliquez sur l'icône **Zoom complet**.

#### Création du deuxième paramètre en entrée : masque de découpe

Dans l'onglet Entrées, double-cliquez à nouveau sur **Couche vecteur** :

[![Fenêtre de définition d'un paramètre](illustrations/11_03_def_parametre2_fenetre.jpg)](illustrations/11_03_def_parametre2_fenetre.jpg "illustrations/11_03_def_parametre2_fenetre.jpg")

* Nom du paramètre : **couche masque**
* Type de géométrie : **polygone**
* **Obligatoire**

Une deuxième boîte apparait aux côtés de la première :

[![Les 2 boîtes pour la couche source et la couche masque](illustrations/11_03_modele_02.jpg)](illustrations/11_03_modele_02.jpg "illustrations/11_03_modele_02.jpg")

#### Création du premier algorithme : découpage

Dans l'onglet **Algorithmes**, rubrique **Recouvrement de vecteur** → double-cliquez sur l'outil **Couper** :

[![Fenêtre du modeleur, onglet algorithmes](illustrations/11_03_modeleur_fenetre_algos.jpg)](illustrations/11_03_modeleur_fenetre_algos.jpg "illustrations/11_03_modeleur_fenetre_algos.jpg")

[![Fenêtre de définition d'un algo](illustrations/11_03_def_algo_fenetre.jpg)](illustrations/11_03_def_algo_fenetre.jpg "illustrations/11_03_def_algo_fenetre.jpg")

* Description : **Couper**
* Couche en entrée : cliquez sur le bouton à gauche pour choisir **Entrée du modèle** à la place de valeur, pour choisir **couche à découper** dans la liste à droite
* Couche de découpage : idem, choisir **Entrée du modèle** puis **couche masque**
* Découpé : ne rentrez rien dans cette partie, pour que la couche créée soit temporaire

L'algorithme apparaît sous forme d'une boîte blanche reliée aux 2 couches en entrée ; de même, vous pouvez éditer ses caractéristiques en double-cliquant sur la boîte.

[![Modèle avec les 3 boîtes pour les 2 couches en entrée et l'algo couper](illustrations/11_03_modele_03.jpg)](illustrations/11_03_modele_03.jpg "illustrations/11_03_modele_03.jpg")

#### Création du second algorithme : modification du SCR

Toujours dans la fenêtre du modeleur de traitement,
 [onglet Algorithmes → Outils généraux pour les vecteur→ Reprojeter une couche

![Emplacement de l'outil 'Reprojeter une couche'](illustrations/11_03_reprojeter.jpg)](#thumb "#thumb")  :

[![Fenêtre de définition d'un algo](illustrations/11_03_def_algo2_fenetre.jpg)](illustrations/11_03_def_algo2_fenetre.jpg "illustrations/11_03_def_algo2_fenetre.jpg")

* Description : **Reprojeter une couche**
* Couche source : cliquez sur le bouton à gauche pour choisir **Sortie d'un algorithme** puis dans la liste à droite **'Découpé' créé par l'algorithme 'Couper'**
* SCR cible : laissez **EPSG:4326**, ce qui correspond au WGS84 (l'idée étant de passer du Lambert 93 au WGS84)
* Reprojecté : tapez le nom de votre choix, par exemple **découpé+reprojeté**

Votre modèle est maintenant fini ! Il doit ressembler à ceci :

[![Modèle fini, avec les 2 boîtes pour les couches en entrée, les 2 boîte pour les algos et la boîte pour la couche en sortie](illustrations/11_03_modele_fini.jpg)](illustrations/11_03_modele_fini.jpg "illustrations/11_03_modele_fini.jpg")

### Enregistrement et documentation d'un modèle

#### Enregistrer un modèle

Comment faire maintenant pour sauvegarder notre modèle ?

[![Fenêtre du modeleur, choix du nom du modèle et du groupe et icône de sauvegarde entourés en rouge](illustrations/11_03_enregistrer_modele_fenetre.jpg)](illustrations/11_03_enregistrer_modele_fenetre.jpg "illustrations/11_03_enregistrer_modele_fenetre.jpg")

Dans l'onglet **Propriétés du modèle** de la partie gauche de la fenêtre, choisissez le nom sous lequel votre modèle sera disponible dans la boîte à outils, par exemple **découper et modifier SCR** par exemple.

Tapez également le nom de son groupe, c'est-à-dire la rubrique dans laquelle votre modèle apparaîtra au sein de la boîte à outils : **tests** par exemple.

Si le groupe n'existe pas déjà, il sera créé.

![icône Enregistrer](illustrations/11_03_enregistrer_modele_icone.jpg)Cliquez ensuite sur l'icône **Enregistrer le modèle sous**. Dans la fenêtre qui s'ouvre alors, choisissez un nom pour votre modèle, par exemple **couper_modifSCR**.

Notez qu'il va être enregistré dans le répertoire par défaut des modèles : processing/models dans le dossier qgis, et qu'il possède l'extension *.model3* (pour QGIS 3).

#### Documenter un modèle

Si ce modèle est destiné à être utilisé par d'autres personnes, ou tout simplement si vous comptez vous en servir régulièrement, documenter un peu ce modèle sera très pratique. Il s'agit en fait de **rédiger l'aide de l'outil**, telle qu'on peut la voir dans la partie droite de la fenêtre pour les outils QGIS.

[![Fenêtre de l'outil Couper, avec la partie Aide à droite entourée en rouge](illustrations/11_03_aide_exemple.jpg)](illustrations/11_03_aide_exemple.jpg "illustrations/11_03_aide_exemple.jpg")
Exemple d'aide : l'outil Couper.

Si vous avez fermé la fenêtre d'édition du modèle, vous pouvez y accéder à nouveau : **boîte à outils → modèles → tests (ou le nom de votre groupe) → clic droit sur le nom de votre outil, Editer le modèle...**

[![Emplacement du modèle dans la boîte à outils](illustrations/11_03_emplacement_modele.jpg)](illustrations/11_03_emplacement_modele.jpg "illustrations/11_03_emplacement_modele.jpg")

Dans la barre d'outils en haut de la fenêtre d'édition du modèle, cliquez sur l'icône **Éditer l'aide du modèle**.

[![Barre d'outils de la fenêtr d'édition du modèle, icône Aide entourée en rouge](illustrations/11_03_modele_aide_icone.jpg)](illustrations/11_03_modele_aide_icone.jpg "illustrations/11_03_modele_aide_icone.jpg")

La fenêtre de l'éditeur d'aide s'ouvre :

[![Fenêtre de l'éditeur d'aide du modèle](illustrations/11_03_aide_fenetre.jpg)](illustrations/11_03_aide_fenetre.jpg "illustrations/11_03_aide_fenetre.jpg")

Cliquez par exemple sur **Description de l'algorithme** à gauche, puis rédigez le texte correspondant à droite.

L'aide doit être courte et claire !

Vous pouvez également rédiger l'aide pour d'autres parties, par exemple pour les 2 paramètres en entrée et le rendu.

Votre modèle est fini et possède même une aide... C'est le moment de le tester !

### Application

#### Découpage et reprojection d'une couche

L'objectif est de découper la couche de routes par la commune, pour ne garder que les routes à l'intérieur de cette commune, la couche obtenue devant être en WGS84.

Si elles ne sont pas déjà chargées, ajoutez à QGIS les couches *OSM_routes* et *SAINTE_RADEGONDE* situées dans le dossier **TutoQGIS_11_Automatisation/donnees**.

Dans quel SCR sont ces deux couches ?

Les 2 couches sont en RGF93 Lambert 93, code EPSG 2154 (cf. [SCR d'une couche](02_03_couches_projets.php#II32 "02_03_couches_projets.php#II32")).

Lancez votre modèle : **boîte à outils → modèles → tests (ou le nom de votre groupe) → double clic sur le nom de votre outil**.

[![fenêtre du modele clip and project, paramètres remplis](illustrations/11_03_test_modele.jpg)](illustrations/11_03_test_modele.jpg "illustrations/11_03_test_modele.jpg")

* couche source : *OSM_routes*
* couche masque : *SAINTE_RADEGONDE*
* découpé+reprojeté : ne tapez rien, pour que le résultat soit une couche temporaire

**Exécutez**, vérifiez le SCR de la couche obtenue, ainsi que son contenu : elle ne doit comporter que les routes à l'intérieur de la commune de Sainte-Radégonde (en gris foncé dans la figure ci-dessous).

[![résultat de la découpe : les 2 couches de route et la couche de commune](illustrations/11_03_resultat_decoupe.jpg)](illustrations/11_03_resultat_decoupe.jpg "illustrations/11_03_resultat_decoupe.jpg")

#### Découpage et reprojection de plusieurs couches (utilisation « par lot »)

Le but est ici de découper et reprojeter plusieurs couches, sans avoir à lancer plusieurs fois le modèle.

A partir de la boîte à outils de traitements, clic droit sur le modèle, **Exécuter comme processus de lot...**. Remplissez les différents paramètres, en vous aidant éventuellement de la [partie XI.2](11_02_par_lot.php "11_02_par_lot.php").

[![remplissage des paramètres de l'outil clip and project en mode par lot](illustrations/11_03_test_modele_lot.jpg)](illustrations/11_03_test_modele_lot.jpg "illustrations/11_03_test_modele_lot.jpg")

Exécutez et vérifiez les couches obtenues.

Les modèles permettent de créer une chaîne de traitement, en enchaînant autant d'algorithmes que vous le souhaitez, et **sont donc très pratiques si vous êtes amenés à répéter souvent la même séquence d'opérations**.

Au-delà de la création du modèle, il peut être utile quand vous réfléchissez à une manipulation de dessiner au papier et crayon l'enchaînement des étapes. Et une fois finalisé de noter le tout dans un fichier texte, pour vous aider à comprendre ce que vous avez fait quand vous reprendrez ce dossier dans 6 mois !

Dans le chapitre suivant, nous allons voir une autre méthode pour automatiser des tâches dans QGIS, plus puissante mais avec un coût d'entrée plus important, en utilisant le langage de programmation Python.

[chapitre précédent](11_02_par_lot.php "11_02_par_lot.php")
[chapitre suivant](11_04_python.php "11_04_python.php")

[haut de page](#wrap "#wrap")
