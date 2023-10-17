
## VI.2 Sélectionner des éléments en fonction de leur position par rapport à d'autres : requêtes spatiales


* [Faire une requête spatiale simple](#VI21 "#VI21")
* [Les opérateurs](#VI22 "#VI22")
* [Quelques exemples](#VI23 "#VI23")




Nous venons de voir comment sélectionner des éléments en fonction des données de la table attributaire ; nous allons voir ici comment sélectionner des éléments en fonction de leur position par rapport aux éléments d'une autre couche.


Contrairement aux requêtes attributaires, les requêtes spatiales mettent donc le plus souvent deux couches en jeu : une couche dans laquelle sera faite la sélection, et une couche de référence.


On peut par exemple, à l'aide d'une couche de points et d'une couche de polygones, sélectionner tous les points situés dans les polygones.


### Faire une requête spatiale simple



Ouvrez un nouveau projet QGIS et ajoutez-y la couche *[communes_Bretagne](donnees/TutoQGIS_06_Requetes.zip "donnees/TutoQGIS_06_Requetes.zip")*.


En vous connectant au [flux WFS](03_02_donnees_flux.php#III23 "03_02_donnees_flux.php#III23") **https://geobretagne.fr/geoserver/dreal_b/wfs**, ajoutez également au projet la couche *Eoliennes implantations en Bretagne*.


Au cas où la connexion au flux échouerait, cette couche est également disponible dans le dossier [TutoQGIS_06_Requetes](donnees/TutoQGIS_06_Requetes.zip "donnees/TutoQGIS_06_Requetes.zip").



[![Eoliennes en Bretagne](illustrations/6_2_eoliennes_bretagne.jpg)](illustrations/6_2_eoliennes_bretagne.jpg "illustrations/6_2_eoliennes_bretagne.jpg")


Le but va être ici de sélectionner toutes les communes de Bretagne sur lesquelles sont implantées une ou plusieurs éoliennes.


**Les données provenant d'un flux, il est possible que vos requêtes donnent des résultats légèrement différents de ceux présentés ici, si le flux a été mis à jour !**



Si la boîte à outils de traitements n'est pas visible, activez-la en vous rendant dans le **menu Traitement → Boîte à outils**.



[![Emplacement de l'outil de sélection par localisation dans la boîte à outils](illustrations/6_2_select_localisation_emplacement.jpg)](illustrations/6_2_select_localisation_emplacement.jpg "illustrations/6_2_select_localisation_emplacement.jpg")

Dans la rubrique **Sélection dans un vecteur**, double-cliquez sur l'outil **Sélection par localisation** :



[![Fenêtre de l'outil de sélection par localisation](illustrations/6_2_select_localisation_fenetre.jpg)](illustrations/6_2_select_localisation_fenetre.jpg "illustrations/6_2_select_localisation_fenetre.jpg")

* **Sélectionnez les entités depuis :** il s'agit de la couche dans laquelle sera faite la sélection, sélectionnez la couche de communes
* **Où les entités :** différents opérateurs sont disponibles. Vous pouvez choisir **intersecte**, ou bien **contient**, pour le même résultat dans ce cas
* **En comparant les entités de :** cette formulation obscure vous invite à choisir la couche par rapport à laquelle vous souhaitez sélectionner des entités, ici la **couche d'éoliennes** puisque nous voulons sélectionner les communes contenant des éoliennes
* Vérifiez que **Créer une nouvelle sélection** soit bien l'option choisie, afin de ne pas partir d'une sélection existante
* Cliquez sur **Exécuter**, vous pouvez ensuite fermer la fenêtre.


Vous devriez obtenir 256 communes sélectionnées (mais ce nombre peut varier légèrement si vous chargez les données via le flux WFS et qu'elles ont été mises à jour depuis la rédaction de ce tutoriel) :



[![Communes sélectionnées](illustrations/6_2_select_localisation_res.jpg)](illustrations/6_2_select_localisation_res.jpg "illustrations/6_2_select_localisation_res.jpg")

Vous pouvez voir le nombre d'entités sélectionnées dans la barre tout en bas de la fenêtre de QGIS :



[![barre du bas avec le nombre d'entités sélectionnées](illustrations/6_2_barre_nb_entites_select.jpg)](illustrations/6_2_barre_nb_entites_select.jpg "illustrations/6_2_barre_nb_entites_select.jpg")

ou bien en haut de la table attributaire des communes :



[![haut de la table attributaire avec le nombre d'entités sélectionnées](illustrations/6_2_table_nb_entites_select.jpg)](illustrations/6_2_table_nb_entites_select.jpg "illustrations/6_2_table_nb_entites_select.jpg")


### Les opérateurs


Dans l'exemple ci-dessus, nous avons utilisé l'opérateur **Intersecte** ou **Contient**. Il en existe d'autres ; les opérateurs possibles varient en fonction de la nature des couches source et de référence (point, ligne, polygone).




Opérateurs de requête spatiale disponibles en fonction des types des couches de de départ et de référence.| Couche de départ : | icône de point | icône de ligne | icône de polygone |
| Couche de référence : | icône de point | icône de ligneicône de polygone | icône de point | icône de ligne | icône de polygone | icône de pointicône de ligne | icône de polygone |
| A l'intérieur | icône faux | icône correct | icône faux | icône faux | icône correct | icône faux | icône correct |
| Chevauche | icône correct | icône faux | icône faux | icône correct | icône faux | icône faux | icône correct |
| Croise | icône faux | icône correct | icône faux | icône correct | icône correct | icône faux | icône faux |
| Contient | icône faux | icône faux | icône correct | icône faux | icône faux | icône correct | icône faux |
| Est disjoint | icône correct | icône correct | icône correct | icône correct | icône correct | icône correct | icône correct |
| Est égal | icône correct | icône faux | icône faux | icône correct | icône faux | icône faux | icône correct |
| Intersecte | icône correct | icône correct | icône correct | icône correct | icône correct | icône correct | icône correct |
| Touche | icône faux | icône correct | icône faux | icône correct | icône correct | icône faux | icône correct |


Par exemple, un point peut se trouver à l'intérieur d'un polygone mais une ligne ne peut se trouver à l'intérieur d'un point.


Pour en savoir plus sur les différents opérateurs, rendez-vous [ici](https://gis.stackexchange.com/questions/217444/understanding-join-attributes-by-location-in-qgis/305193#305193 "https://gis.stackexchange.com/questions/217444/understanding-join-attributes-by-location-in-qgis/305193#305193") ou [là](https://github.com/boundlessgeo/workshops/blob/master/workshops/postgis/source/en/spatial_relationships.rst#spatial-relationships "https://github.com/boundlessgeo/workshops/blob/master/workshops/postgis/source/en/spatial_relationships.rst#spatial-relationships") (en anglais, mais les dessins sont parlants !).


### Quelques exemples



[Connectez-vous au flux WFS](03_02_donnees_flux.php#III23 "03_02_donnees_flux.php#III23") **http://services.sandre.eaufrance.fr/geo/zonage** et ajoutez la couche *Cours d'eau de plus de 100km - BD Carthage - France entière*.


Ajoutez également si ça n'est pas déjà fait la couche *[DEPARTEMENT](donnees/TutoQGIS_06_Requetes.zip "donnees/TutoQGIS_06_Requetes.zip")*.


Votre projet doit donc contenir les 4 couche suivantes :



[![CProjet avec les 4 couches chargées](illustrations/6_2_projet.jpg)](illustrations/6_2_projet.jpg "illustrations/6_2_projet.jpg")

En utilisant différents opérateurs, pouvez-vous dire ?...


Entre deux requêtes, n'oubliez pas de tout désélectionner :![icône de désélection](illustrations/6_3_deselection_icone.jpg)


Attention, le nombre d'entités sélectionnées peut varier légèrement si vous chargez des données via des flux WFS et que ces données ont été mises à jour depuis la rédaction de ce tutoriel.




Combien de communes bretonnes sont traversées par des cours d'eau de plus de 100 km ?


Sélection des communes qui intersectent les cours d'eau : **447 communes sélectionnées**.


![Communes intersectant les cours d'eau](illustrations/6_2_communes_inters_coursdeau.jpg)





Combien de cours d'eau de plus de 100 km traversent la Bretagne ?


Sélection des cours d'eau qui intersectent les communes (ou les départements bretons préalablement sélectionnés) : **68 cours d'eau sélectionnés**.


![Cours d'eau de intersectant les communes](illustrations/6_2_coursdeau_inters_communes.jpg)





Combien de communes ne contiennent pas d'éoliennes ?


Sélection des communes disjointes des éoliennes : **952 communes sélectionnées**


![icône inverser la sélection](illustrations/6_2_inverser_selection_icone.jpg)Vous pouvez aussi repartir des communes contenant des éoliennes, et **inverser la sélection** avec le bouton correspondant en haut de la table attributaire des communes.


![Communes sans éoliennes](illustrations/6_2_communes_disjoint_eoliennes.jpg)





Combien le département du Finistère contient-il d'éoliennes ?


Il faut procéder en 2 étapes : 1/ sélectionner « à la main » le département du Finistère 2/ utiliser l'outil de sélection par localisation pour sélectionner les éoliennes à l'intérieur des départements, en cochant la case **Entités sélectionnées uniquement**.


![Eoliennes du Finistère](illustrations/6_2_eoliennes_finistere.jpg)


Au final, on trouve **656 éoliennes sélectionnées**.




Dans le chapitre suivant, nous verrons comment combiner une ou plusieurs requêtes, spatiales ou attributaires !




[chapitre précédent](06_01_req_attrib.php "06_01_req_attrib.php")
[chapitre suivant](06_03_req_combinees.php "06_03_req_combinees.php")


[haut de page](#wrap "#wrap")
