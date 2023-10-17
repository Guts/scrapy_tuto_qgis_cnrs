
## X.2 Mettre en page une carte


* [Préparation de la mise en page](#X21 "#X21")
* [Mise en page : une fenêtre dédiée](#X22 "#X22")
* [Modifier les dimensions de la page](#X23 "#X23")
* [Ajouter une carte](#X24 "#X24")
* [Ajouter une légende](#X25 "#X25")
	+ [Création de la légende](#X25a "#X25a")
	+ [Modifier les éléments](#X25b "#X25b")
	+ [Ajouter un titre](#X25c "#X25c")
	+ [Autres paramètres de la légende](#X25d "#X25d")
* [Ajouter une échelle](#X26 "#X26")
	+ [Création de l'échelle](#X26a "#X26a")
	+ [A chaque échelle son style](#X26b "#X26b")
* [Ajout d'éléments supplémentaires : titre, logo, flèche nord...](#X27 "#X27")
* [Ajout d'une carte de situation](#X28 "#X28")
* [Exporter la carte](#X29 "#X29")
* [Sauvegarder une mise en page](#X210 "#X210")


Une fois vos données représentées de manière satisfaisante, il peut être utile d'en faire une carte. **Cette partie n'a pas pour but d'expliquer les bonnes et mauvaises pratiques en matière de cartographie**, mais se bornera à décrire quelques fonctionnalités du mode mise en page de QGIS.


L'exemple portera ici sur une carte de la densité de population par communes (carte choroplèthe) en France. Mais vous pouvez choisir le sujet de votre choix, avec vos données !


### Préparation de la mise en page



Commencez par ajouter toutes les couches dont vous avez besoin, et supprimez toutes les couches inutiles.


Choisissez le style de chacune des couches.


N'oubliez pas également de choisir un SCR adapté pour votre projet (projeté si vous souhaitez créer une échelle en mètres par exemple) (cf. [Modifier le SCR du projet](02_04_changer_systeme.php#II41 "02_04_changer_systeme.php#II41")).


Pour aller plus vite, vous pouvez ouvrir le projet tout fait [misenpage_densite.qgz](donnees/TutoQGIS_10_Representation.zip "donnees/TutoQGIS_10_Representation.zip"). Dans ce cas, nombre des étapes décrites ci-dessous seront déjà réalisées, mais vous pourrez modifier les différents paramètres.



### Mise en page : une fenêtre dédiée


Le mode mise en page ouvre une fenêtre à part dans QGIS. On peut y ajouter différents éléments : carte, légende, échelle... La carte est liée à celle de la fenêtre principale de QGIS et se met à jour automatiquement.


Dans la version 2.18 de QGIS, le mode mise en page se nommait « composeur d'impression ».



Si vous partez du projet tout fait [misenpage_densite.qgz](donnees/TutoQGIS_10_Representation.zip "donnees/TutoQGIS_10_Representation.zip"), ouvrez la mise en page déjà présente dans ce projet : **menu Projet → Mises en page → densité de population**.


Sinon, créez une nouvelle mise en page : **menu Projet → Nouvelle mise en page...** Tapez un titre, par exemple densité communes.


La fenêtre de mise en page s'ouvre (ici pour la mise en page déjà existante) :



[![Fenêtre de mise en page, avec des numéros pour les différentes parties (menus et outils, carte...)](illustrations/10_02_misenpage_general.jpg)](illustrations/10_02_misenpage_general.jpg "illustrations/10_02_misenpage_general.jpg")


On trouve dans cette fenêtre :


*1.* **Menus et barres d'outils :** on retrouve les mêmes outils dans les menus ou via les icônes.


*2.* **Mise en page :** cette zone correspond à une page blanche, dont vous pouvez paramétrez notamment les dimensions. Vous pouvez ajouter à cette page des cartes (liées à la fenêtre principale de QGIS), légendes, échelles etc.


*3.* **Onglet Eléments :** cet onglet comporte la liste des éléments présents sur la page (carte, légende etc.). Vous pouvez les rendre visibles ou invisibles, verrouillés ou non, et en modifier l'ordre.


*4.* **Onglet Historique :** retrouvez ici la liste des dernières opérations que vous avez effectuées, par exemple modifier l'ordre des éléments. En cliquant sur une opération, vous l'effectuez à nouveau.


*5.* **Onglet Mise en page :** cet onglet permet notamment de définir une grille d'accrochage, et une résolution pour l'export. Le contenu de cet onglet ne change jamais.


*6.* **Onglet Propriétés de l'objet :** cet onglet contient les propriétés de l'objet actuellement sélectionné, son contenu varie donc en fonction du type d'objet : carte, légende, texte...


*7.* **Onglet Atlas :** QGIS possède un mode Atlas, très pratique si vous avez une série de cartes à faire sur des zones différentes. Nous n'aborderons pas son fonctionnement, mais vous pouvez en savoir plus par exemple [ici](https://docs.qgis.org/latest/fr/docs/training_manual/forestry/forest_maps.html?highlight=atlas "https://docs.qgis.org/latest/fr/docs/training_manual/forestry/forest_maps.html?highlight=atlas").


*8.* **Barre d'état :** vous pouvez lire ici les coordonnées de votre souris dans la page (il ne s'agit pas de coordonnées géographiques, mais de coordonnées en mm par rapport au coin en haut à gauche de la page) et vous pourrez aussi modifier le niveau de zoom sur la page.


### Modifier les dimensions de la page


La première étape consiste à déterminer les dimensions de la page. Par défaut, il s'agit d'un A4 paysage, mais s'il s'agit d'une figure destinée à être intégrée dans un rapport, vous pouvez très bien choisir une taille personnalisée, par exemple 20 x 20 cm.



Faites un **clic droit sur la page → Propriétés de la page**.



[![Fixer la taille de la page dans la mise en page](illustrations/10_02_taille_page.jpg)](illustrations/10_02_taille_page.jpg "illustrations/10_02_taille_page.jpg")

* Taille : choisissez **Personnalisation** tout en bas de la liste
* Largeur et hauteur : **200 mm**


![icône zoom sur l'emprise totale de la page](illustrations/10_02_zoom_page_icone.jpg)Pour zoomer sur votre page : cliquez sur l'icône **Zoom complet** (ou **menu Vue → Zoom sur l'emprise totale**).



### Ajouter une carte



![icône ajouter une nouvelle carte](illustrations/10_02_nouvelle_carte_icone.jpg)Cliquez ensuite sur l'icône **Ajouter Carte** (ou **menu Ajouter un objet → Ajouter Carte**).


Dessinez un rectangle n'importe où sur la page, de la taille que vous voulez. Puis rendez-vous dans l'onglet **Propriétés de l'objet**, rubrique **Position et taille** (vers le bas de l'onglet).


Fixez **X et Y à 0** et la **largeur et hauteur à 200 mm** pour que la carte coïncide avec la page.



[![Fixer l'emplacement et la taille de la carte sur la page](illustrations/10_02_position_carte.jpg)](illustrations/10_02_position_carte.jpg "illustrations/10_02_position_carte.jpg")


**La carte ainsi créée est synchronisée avec les données visibles dans QGIS** : si vous changer le style d'une des couches dans la fenêtre principale de QGIS et revenez à la mise en page, la carte aura été mise à jour (si besoin en cliquant sur le bouton actualiser).



![icône déplacer le contenu de l'objet](illustrations/10_02_deplacer_contenu_icone.jpg)Pour **centrer la carte** : cliquez sur l'icône **Déplacer le contenu de l'objet** et faites glisser le contenu de la carte.


Pour **zoomer et dézoomer**, 3 méthodes :


* pour un zoom « à la louche », utilisez la **molette** de la souris après avoir sélectionné l'outil **Déplacer le contenu de l'objet**
* ![Icône de l'outil de sélection du mode mise en page](illustrations/10_02_selection_deplace_icone.jpg)pour un zoom plus précis : sélectionnez la carte au moyen de l'**outil de sélection**, puis **modifiez l'échelle** dans l'onglet Propriétés de l'objet → Propriétés principales
 [![Fixer l'échelle de la carte](illustrations/10_02_zoom.jpg)](illustrations/10_02_zoom.jpg "illustrations/10_02_zoom.jpg")
* Synchroniser la carte de la mise en page avec celle de la fenêtre principale de QGIS : cliquez sur la 2ème icône dans la barre d'outils en haut des propriétés de l'objet :
 [![Fixer l'échelle de la carte sur celle de la fenêtre QGIS](illustrations/10_02_zoom2.jpg)](illustrations/10_02_zoom2.jpg "illustrations/10_02_zoom2.jpg")


Il est probable que les 2 cartes ne coïncident pas exactement car elles n'ont pas le même rapport hauteur/largeur. Vous pouvez aussi cliquer sur la 4ème icône pour donner à la carte de votre mise en page la même échelle que dans la fenêtre principale QGIS.



### Ajouter une légende


Il existe de nombreuses possibilités pour paramétrer la légende. Elles ne seront pas toutes passées en revue ici, mais n'hésitez pas à explorer par vous-même !


#### Création de la légende



![icône ajouter légende](illustrations/10_02_legende_icone.jpg)Pour ajouter une **légende** : icône **Ajouter Légende**, puis cliquez n’importe où sur la carte.


La fenêtre **Propriétés de l'élément** s'ouvre : cliquez sur OK sans modifiez les paramètres, ce que vous pourrez toujours faire par la suite.


La légende reprend celle de la couche dans QGIS : si vous modifiez les étiquettes de la légende dans la propriété de la couche, la légende de la mise en page prendra en compte ces modifications.


Dans la fenêtre principale de QGIS, ouvrez les propriétés de la couche, rubrique Style. Vous pouvez :


* **Modifier les bornes des classes** en double-cliquant sur une ligne dans la colonne valeur
* **Modifier l'étiquette des classes** en double-cliquant sur une ligne dans la colonne étiquette



[![Modifier les bornes des classes et leurs étiquettes dans les propriétés de la couche](illustrations/10_02_style_etiquettes.jpg)](illustrations/10_02_style_etiquettes.jpg "illustrations/10_02_style_etiquettes.jpg")

![icône sélectionner/déplacer un objet](illustrations/10_02_selection_deplace_icone.jpg)Revenez ensuite dans la mise en page, les changements que vous avez effectués sont visibles dans la légende puisque la case **Mise à jour auto** est cochée par défaut.



#### Modifier les éléments


Comment faire maintenant si vous désirez encore modifier les éléments de la légende ?


La case **Mise à jour auto** permet de prendre en compte directement les changements effectués dans la fenêtre principale de QGIS.


Cette case présente néanmoins l'inconvénient de ne pas vous donner la main sur la légende ; si vous la décochez, vous pourrez changer l'ordre des couches, en ajouter et en supprimer... grâce aux icônes situées sous la légende, et mettre à jour leur légende s'il y a eu modification dans QGIS en cliquant sur le bouton **Tout mettre à jour**.



Cliquez sur votre légende avec l'outil **Sélectionner / Déplacer un objet**.


Décochez la case **Mise à jour auto**. Les outils sous la légende sont maintenant activés :



[![Rubrique objets de légende dans les propriétés de la légende](illustrations/10_02_objets_legende.jpg)](illustrations/10_02_objets_legende.jpg "illustrations/10_02_objets_legende.jpg")

Vous pouvez maintenant, au moyen de ces outils :


![2 icônes pour monter ou descendre les éléménts de la légende](illustrations/10_02_legende_ordre_icone.jpg)**Modifier l'ordre** des éléments dans la légende : utile pour mettre les éléments plus importants en premier


![icône pour créer des groupes dans la légende](illustrations/10_02_legende_groupe_icone.jpg)**Créer des groupes**, pour hiérarchiser l'information


![icône pour ajouter des éléments dans la légende](illustrations/10_02_legende_plus_icone.jpg)**Ajouter des couches** présentes dans QGIS et non visibles dans la légende


![icône pour supprimer des éléments de la légende](illustrations/10_02_legende_moins_icone.jpg)**Supprimer des couches** de la légende, par exemple ici la couche *ne_10m_land*, qui n'apporte rien à la compréhension de la carte en étant présente dans la légende


![icône pour modifier le texte des éléments de la légende](illustrations/10_02_legende_texte_icone.jpg)**Modifier le texte** des éléments, si vous ne l'avez pas déjà fait dans QGIS, par exemple densité de population à la place de COMMUNE


![icône pour compter le nombre d'entités dans la légende](illustrations/10_02_legende_compter_icone.jpg)**Afficher le nombre d'entités** dans une couche et éventuellement dans chaque classe, après avoir sélectionné une couche


![icône pour filtrer les éléments de la légende en fonction de la carte](illustrations/10_02_legende_filtrecarte_icone.jpg)**Filtrer la légende en fonction de ce qui est visible sur la carte**


![icône pour filtrer les éléments de la légende en fonction d'une expression](illustrations/10_02_legende_filtrexpression_icone.jpg)**Filtrer la légende en fonction d'une expression**



#### Ajouter un titre


Parfois, il peut être utile d'ajouter un titre à la légende ; dans d'autre cas, le nom de la couche peut suffire.


**Dans tous les cas, évitez d'écrire « Légende »**, ce qui n'apporte rien à la carte puisqu'on voit bien qu'il s'agit de la légende. Préférez un titre indiquant clairement le sujet de la carte.



Dans les propriétés de la légende Propriétés principales, vous pouvez taper un titre.


Si vous voulez que ce titre soit sur plusieurs lignes, vous pouvez taper un caractère utilisé rarement dans la case **Activer le retour à la ligne après**. Ce caractère ne sera pas représenté mais provoquera un retour à la ligne.



[![Exemple de titre de légende avec un retour à la ligne](illustrations/10_02_legende_titre.jpg)](illustrations/10_02_legende_titre.jpg "illustrations/10_02_legende_titre.jpg")

Le $ provoquera également une retour à la ligne pour les autres objets de la légende (étiquettes, nom de la couche...).



#### Autres paramètres de la légende


Il est possible de modifier beaucoup de paramètres de la légende, comme par exemple la police, l'espacement des éléments...



[![Dans l'onglet propriétés de l'objet, paramètres de la légende de 'Polices' à 'Variables'](illustrations/10_02_legende_autreparametres.jpg)](illustrations/10_02_legende_autreparametres.jpg "illustrations/10_02_legende_autreparametres.jpg")

Voici quelques uns de ces éléments passés en revue, n'hésitez pas à tester !


* **Fonts (Polices)** : vous pouvez choisir la police, la taille et le style pour le titre, les groupes etc.
* **Colonnes** : pour une légende sur plusieurs colonnes
* **Symbole** : pour modifier la taille des symboles de légende
* **Espacement** : pour augmenter ou diminuer l'espace entre les différents éléments (par exemple sous le titre)
* **Cadre** : pour encadrer ou non la légende
* **Arrière-plan** : pour enlever ou choisir la couleur d'arrière-plan. Cette couleur peut avoir de la transparence.


Un exemple de légende :



[![Exemple de légende pour la densité de population](illustrations/10_02_legende_visu.jpg)](illustrations/10_02_legende_visu.jpg "illustrations/10_02_legende_visu.jpg")

### Ajouter une échelle


Pour certaines cartes, une échelle peut aider le lecteur à mieux comprendre le phénomène représenté. **Dans d'autres, elle ne sera pas nécessaire** (par exemple une carte du monde pour un public déjà familier de ce type de carte).


On trouve 2 types d'échelles : **numérique**, de type 1/25000, ou **graphique**, avec une barre d'échelle. La barre d'échelle est généralement plus claire, et présente l'avantage d'être toujours valable si votre document est imprimé à une taille différente de l'original. QGIS permet la création de ces 2 types d'échelles.


Attention, si vous utilisez une projection ne conservant pas les distances, votre échelle ne sera pas valable partout. Il est dans ce cas d'usage de préciser par exemple « échelle valable à l'équateur ».


#### Création de l'échelle



![icône ajouter une nouvelle échelle graphique](illustrations/10_02_echelle_icone.jpg)Pour ajouter une échelle : outil **Ajouter Barre d'échelle** puis dessinez un rectangle sur la carte.


Cliquez sur **OK** dans la fenêtre des propriétés de l'élément qui s'ouvre ensuite (vous pourrez toujours modifier ces paramètres par la suite).


Modifiez ensuite éventuellement la taille du rectangle de l'échelle, en cliquant sur un des bords et en maintenant la souris enfoncée :



[![Réduire la taille de l'échelle en cliquant sur le bord](illustrations/10_02_echelle_reduire.jpg)](illustrations/10_02_echelle_reduire.jpg "illustrations/10_02_echelle_reduire.jpg")


Comme pour la légende, il est possible de régler assez finement les différents paramètres de cette échelle.


#### A chaque échelle son style



![icône sélectionner/déplacer un objet](illustrations/10_02_selection_deplace_icone.jpg)Après avoir sélectionné l'échelle au moyen de l'outil de sélection, vous pouvez en modifier les propriétés dans l'onglet **Propriétés de l'objet.**


Vous pouvez notamment modifier son style, ce qui vous permet de choisir entre 5 styles d'échelle graphique et un type d'échelle numérique, le style par défaut étant **Boîte unique** :



[![Où modifier le style de l'échelle](illustrations/10_02_echelle_style.jpg)](illustrations/10_02_echelle_style.jpg "illustrations/10_02_echelle_style.jpg")

Testez les différents styles :



[![Echelle style boîte unique](illustrations/10_02_echelle_boiteunique.jpg)](illustrations/10_02_echelle_boiteunique.jpg "illustrations/10_02_echelle_boiteunique.jpg")
[![Echelle style boîte double](illustrations/10_02_echelle_boitedouble.jpg)](illustrations/10_02_echelle_boitedouble.jpg "illustrations/10_02_echelle_boitedouble.jpg")
[![Echelle style repère au milieu de la ligne](illustrations/10_02_echelle_reperemilieu.jpg)](illustrations/10_02_echelle_reperemilieu.jpg "illustrations/10_02_echelle_reperemilieu.jpg")
[![Echelle style repère au dessous de la ligne](illustrations/10_02_echelle_reperedessous.jpg)](illustrations/10_02_echelle_reperedessous.jpg "illustrations/10_02_echelle_reperedessous.jpg")
[![Echelle style repère au dessus de la ligne](illustrations/10_02_echelle_reperedessus.jpg)](illustrations/10_02_echelle_reperedessus.jpg "illustrations/10_02_echelle_reperedessus.jpg")
[![Echelle style numérique](illustrations/10_02_echelle_numerique.jpg)](illustrations/10_02_echelle_numerique.jpg "illustrations/10_02_echelle_numerique.jpg")


Vous pouvez également modifier les unités de l'échelle, et l'étiquette des unités :



[![Paramétrer les unités de l'échelle](illustrations/10_02_echelle_unites.jpg)](illustrations/10_02_echelle_unites.jpg "illustrations/10_02_echelle_unites.jpg")

Ainsi que le nombre de segments, et la hauteur de la barre d'échelle :



[![Paramétrer le nombre de segments de l'échelle](illustrations/10_02_echelle_segments.jpg)](illustrations/10_02_echelle_segments.jpg "illustrations/10_02_echelle_segments.jpg")

Sans oublier les couleurs, et la police de caractères :



[![Paramétrer les couleurs et la taille de l'échelle](illustrations/10_02_echelle_police.jpg)](illustrations/10_02_echelle_police.jpg "illustrations/10_02_echelle_police.jpg")

Et bien d'autres paramètres encore !


Vous pouvez opter pour un style épuré...



[![Exemple d'échelle simple](illustrations/10_02_echelle_visu.jpg)](illustrations/10_02_echelle_visu.jpg "illustrations/10_02_echelle_visu.jpg")

...ou bien laisser parler l'artiste qui est en vous :



[![Exemple d'échelle simple](illustrations/10_02_echelle_coupemulet.jpg)](illustrations/10_02_echelle_coupemulet.jpg "illustrations/10_02_echelle_coupemulet.jpg")

(Notez bien que je décline toute responsabilité dans ce cas)


### Ajout d'éléments supplémentaires : titre, logo, flèche nord...



![icône ajouter une étiquette](illustrations/10_02_etiquette_icone.jpg)Pour ajouter du **texte**, par exemple un titre, les sources, l'auteur... : outil **Ajouter Etiquette**.


Dans les propriétés de cet objet, vous pouvez ensuite modifier le texte, la police, la couleur...


![icône ajouter une image](illustrations/10_02_image_icone.jpg)Si vous voulez ajouter une image, par exemple un logo : outil **Ajouter Image** puis dessinez un rectangle sur la page.


Dans les propriétés principales, choisissez ensuite une image sur votre ordinateur. Attention, il faut choisir **image raster** si votre image est au format JPG, PNG... ou bien **image SVG** si elle est au format vectoriel SVG.


Pour une image raster :



[![Choix d'une image raster](illustrations/10_02_ajout_image_raster.jpg)](illustrations/10_02_ajout_image_raster.jpg "illustrations/10_02_ajout_image_raster.jpg")

Pour une image SVG :



[![Choix d'une image vecteur](illustrations/10_02_ajout_image_svg.jpg)](illustrations/10_02_ajout_image_svg.jpg "illustrations/10_02_ajout_image_svg.jpg")


Par convention, le Nord est situé en haut de votre carte. Ajouter une flèche Nord si tel est bien le cas n'est donc pas indispensable et peut même alourdir inutilement votre carte. Par ailleurs, suivant la projection que vous utilisez, la flèche Nord peut ne pas être valable pour toute la carte, mais par exemple seulement le long du méridien de référence.


Peut-être avez-vous néanmoins besoin d'une flèche Nord, par exemple si le Nord n'est pas en haut de votre carte ?



Dans ce cas, utilisez également l'outil **Ajouter Image** et choisissez comme image un symbole de flèche Nord. Pour cela, vous pouvez regarder dans les groupes SVG **arrows** ou **wind roses**.



[![Choix d'un symbole de fleche nord à partir de la bibliotheque de symboles](illustrations/10_02_fleche_nord.jpg)](illustrations/10_02_fleche_nord.jpg "illustrations/10_02_fleche_nord.jpg")

Il est possible d'ajouter de nouveaux symboles au format SVG à cette bibliothèque, au moyen du bouton **...** situé au-dessous.


Pour que cette flèche Nord soit synchronisée avec la carte, si la carte présente une rotation, descendez jusqu'à la rubrique rotation et cochez **Synchroniser avec la carte** :



[![Synchronisation de la rotation de la flèche nord avec la carte](illustrations/10_02_nord_rotation.jpg)](illustrations/10_02_nord_rotation.jpg "illustrations/10_02_nord_rotation.jpg")

Si la carte présente une rotation (à spécifier dans ses propriétés, toujours dans la mise en page), la flèche aura cette même rotation.



### Ajout d'une carte de situation


Vous pouvez également ajouter une deuxième carte à votre page, qui servira par exemple de carte de situation.


Il est possible de faire figurer dans cette deuxième carte un rectangle correspondant à l'emprise de la première carte.



[![exemple : une carte de France, avec en haut une petite carte d'Europe et un rectangle correspondant à l'emprise de la carte de France](illustrations/10_02_apercu.jpg)](illustrations/10_02_apercu.jpg "illustrations/10_02_apercu.jpg")


Ajoutez une carte, réglez son emprise et son échelle, et allez dans la rubrique **Aperçu** des propriétés de cette carte, pour visualiser l'emprise de votre première carte dans cette deuxième carte :



[![reglage de l'aperçu pour voir l'emprise de la 1ère carte sur la 2ème](illustrations/10_02_apercu_reglage.jpg)](illustrations/10_02_apercu_reglage.jpg "illustrations/10_02_apercu_reglage.jpg")

* Cliquez sur le bouton **+** pour ajouter un aperçu
* Choisissez la carte dont vous voulez voir l'emprise dans cette carte. Dans cet exemple, il s'agit de **Carte 1**
* Modifiez éventuellement le style de cadre



Avec plusieurs cartes, il faut gérer la visibilité des couches dans chacune des cartes.



Pour cela, vous pouvez utiliser cette méthode :


* Dans QGIS, créez autant de groupes que de cartes dans votre mise en page (clic droit dans la liste des couches, Ajouter un groupe), ici un groupe **carte principale** et un groupe **carte de situation**
* Dans QGIS, mettez dans chacun des groupes les couches que vous voulez voir figurer dans la mise en page correspondante, quitte à dupliquer certaines couches (clic droit, Dupliquer la couche)



![2 groupes de couches dans QGIS](illustrations/10_02_groupes_qgis.jpg)

* Toujours dans QGIS, rendez visible uniquement les couches d'un groupe
* Dans le mode mise en page, sélectionnez la carte correspondant au groupe visible dans QGIS, et cochez la case **Verrouiller les couches** dans la rubrique **Couches** des propriétés de la carte



![case pour verrouiller les couches dans les propriétés de la carte](illustrations/10_02_verrouiller_couches.jpg)

* Faites de même pour les autres groupes



### Exporter la carte


Vous êtes satisfait de votre carte ? Voici venu le moment de l'exporter !


Vous pouvez soit l'**exporter au format image** (PNG, JPG) pour l'intégrer directement dans un rapport par exemple, soit l'**exporter au format vectoriel** SVG ou PDF pour la retravailler dans un logiciel de dessin type Inkscape ou Adobe Illustrator. Vous pouvez également l'imprimer directement !



Pour **exporter au format image** : vous pouvez tout d'abord paramétrer la résolution à laquelle votre carte sera exportée : onglet **Mise en page**, **Paramètres d'export :**



[![choix d'une résolution de 300 dpi pour l'export](illustrations/10_02_export_resolution.jpg)](illustrations/10_02_export_resolution.jpg "illustrations/10_02_export_resolution.jpg")

On considère généralement qu'une résolution de 300 dpi est suffisante pour une impression. Pour en savoir plus sur ce qu'est la résolution d'une image : [http://fr.wikipedia.org/wiki/R%C3%A9solution_%28imagerie_num%C3%A9rique%29](http://fr.wikipedia.org/wiki/R%C3%A9solution_%28imagerie_num%C3%A9rique%29 "http://fr.wikipedia.org/wiki/R%C3%A9solution_%28imagerie_num%C3%A9rique%29")


![icône Exporter comme une image](illustrations/10_02_export_image_icone.jpg)Pour ensuite exporter votre mise en page au format image : à partir de la fenêtre de mise en page, **menu Mise en page → Exporter au format image...**


De nombreux formats sont disponibles : PNG, JPEG, TIFF...



Si vous voulez pouvoir modifier votre carte dans un logiciel de dessin vectoriel, il faut l'exporter dans un format vectoriel, SVG ou PDF.



![icône Exporter au format SVG](illustrations/10_02_export_svg_icone.jpg)Pour **exporter au format SVG** : **menu mise en page → Exporter au format SVG...**



L'export au format SVG peut poser quelques problèmes, en particulier pour gérer la transparence. L'export au format PDF peut parfois être plus pratique pour ensuite retoucher la carte dans un logiciel de dessin.



![icône Exporter au format PDF](illustrations/10_02_export_pdf_icone.jpg)Pour **exporter au format PDF** : **menu mise en page → Exporter au format PDF...**



Vous pouvez également imprimer directement votre carte, par exemple pour tester son rendu.



![icône Imprimer](illustrations/10_02_impression_icone.jpg)Pour **imprimer la carte** : **menu mise en page → Imprimer...** ou bien **Ctrl + P**



Un exemple de carte réalisée dans QGIS :



[![exemple d'une carte de densité de population dans QGIS](illustrations/10_02_carte_exemple.jpg)](illustrations/10_02_carte_exemple.jpg "illustrations/10_02_carte_exemple.jpg")

### Sauvegarder une mise en page


Dans QGIS, les mises en page sont sauvegardées dans les projets QGZ ou QGS. Pour sauvegarder votre mise en page, il vous suffit donc de sauvegarder votre projet.



Dans la fenêtre principale de QGIS, rendez-vous dans le **menu Projet → Enregistrer sous...**.


Choisissez un emplacement : dossier **TutoQGIS_10_Representation/projets** par exemple, et un nom : **carte_densite_01** par exemple.


Un projet peut contenir plusieurs mises en page. Pour renommer, ajouter, supprimer ou dupliquer des mises en page : **menu Projet → Gestionnaire de mise en page...**.



[![Fenêtre du gestionnaire de mise en page](illustrations/10_02_gestionnaire_misenpage.jpg)](illustrations/10_02_gestionnaire_misenpage.jpg "illustrations/10_02_gestionnaire_misenpage.jpg")


Vous savez maintenant présenter vos travaux de manière claire, bravo ! Le chapitre suivant traitera d'un tout autre sujet, à savoir l'automatisation de tâches dans QGIS...




[chapitre précédent](10_01_representation.php "10_01_representation.php")
[partie XI : automatisation de traitements](11_00_automatisation.php "11_00_automatisation.php")


[haut de page](#wrap "#wrap")
