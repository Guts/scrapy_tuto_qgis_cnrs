
## V.3 Saisie des données attributaires : en savoir plus


* [Saisir les données : à la création de l'entité ou dans la table](#V31 "#V31")
* [Pour une saisie plus facile : les outils d'édition](#V32 "#V32")




Cette partie est tout à fait optionnelle pour suivre la suite du chapitre. Elle pourra néanmoins vous faire gagner du temps si vous vous apprêtez à saisir des données sous QGIS...


### Saisir les données : à la création de l'entité ou dans la table


Vous avez remarqué que la saisie des données attributaires se fait dans une fenêtre qui apparaît directement après avoir créé une entité.


Il est possible de modifier ce comportement :



Rendez-vous dans le menu
 [Menu Préférences → Options

![Menu Préférences, Options](illustrations/5_3_options_menu.jpg)](#thumb "#thumb")
 :



[![Fenêtre Options, rubrique numérisation](illustrations/5_3_options_fenetre.jpg)](illustrations/5_3_options_fenetre.jpg "illustrations/5_3_options_fenetre.jpg")

Dans la rubrique **Numérisation**, cochez la case **Supprimer la fenêtre de saisie des attributs lors de la création de chaque entité**. Cliquez sur **OK** pour valider et fermer la fenêtre.


Créez un nouveau point dans la couche de bâtiments : aucune fenêtre ne s'affiche. Si vous ouvrez la table attributaire, vous pouvez voir que le point créé a un type NULL (valeur par défaut).



Il est ensuite possible de rentrer les données attributaires directement dans la table. La [calculatrice de champ](07_02_calculer.php "07_02_calculer.php") offre la possibilité de remplir plusieurs cases avec une requête.


### Pour une saisie plus facile : les outils d'édition


Il est possible de définir des règles pour la saisie d'attributs : vous pouvez par exemple saisir vos données en choisissant une valeur dans une liste déroulante.



Ouvrez les propriétés de la couche *batiments_oahu* créée en [V.1](05_01_creation_couche.php "05_01_creation_couche.php"), rubrique **Formulaire d'attributs**.



Cette fenêtre propose différents outils pour faciliter la saisie. Le mode **Edition de texte** est le mode par défaut que vous avez utilisé jusqu'ici.


Par exemple, il est possible de faciliter la saisie de date à l'aide d'un calendrier, de voir un champ sous forme de case à cocher, de créer des listes déroulantes...


Sans passer en revue tous les outils possibles, nous nous bornerons à créer une **liste déroulante** avec les deux valeurs « école » et « poste » .




[![propriétés de la couche, rubrique formulaire d'attributs](illustrations/5_3_formulaire_fenetre.jpg)](illustrations/5_3_formulaire_fenetre.jpg "illustrations/5_3_formulaire_fenetre.jpg")

Sélectionnez le champ **type** dans la partie gauche de la fenêtre.


Sélectionnez ensuite **Liste de valeurs** dans la partie **Type d'outil** à droite.


Ajoutez les valeurs **école** et **poste** dans la colonne **Valeur** du tableau (vous pouvez laisser la colonne Description vide).


Cliquez sur **OK**.


Passez en mode édition si ce n'est pas déjà fait. Ouvrez la table attributaire.


Double-cliquez dans une case : une liste déroulante avec les deux valeurs poste et école apparaît.



[![la liste qui apparaît quand on clique sur une case](illustrations/5_3_liste.jpg)](illustrations/5_3_liste.jpg "illustrations/5_3_liste.jpg")


Notez que cette liste déroulante sera également utilisable dans la fenêtre de saisie des attributs, si la case **Supprimer les fenêtres d'avertissement lors de la création de chaque entité** des options de numérisation est décochée (cf. plus haut).



[![la fenêtre de saisie des attributs, avec la liste déroulante](illustrations/5_3_liste_fenetre.jpg)](illustrations/5_3_liste_fenetre.jpg "illustrations/5_3_liste_fenetre.jpg")

Pour en savoir plus, les différents outils d'édition sont décrits dans le [manuel QGIS](https://docs.qgis.org/3.22/fr/docs/user_manual/working_with_vector/vector_properties.html#configure-the-field-behavior "https://docs.qgis.org/3.22/fr/docs/user_manual/working_with_vector/vector_properties.html#configure-the-field-behavior").


Dans le chapitre suivant, dessinez des lignes avec QGIS !




[chapitre précédent](05_02_points.php "05_02_points.php")
[chapitre suivant](05_04_lignes.php "05_04_lignes.php")


[haut de page](#wrap "#wrap")
