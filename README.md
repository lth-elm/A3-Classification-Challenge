# Challenge de Classification

## Présentation

L'objectif est de tester nos implémentations des K plus proches voisins (**k-nn**) sur un dataset anonymisé.

On dispose d'un premier dataset [data.csv](./Data/data.csv) possédant **4 variables d'entrée** et **une variable qualitative en sortie** avec **10 classes** possibles. A nous de le couper en deux ensembles
**train/test** afin de l'entrainer, faire varier des paramètres de notre approche et l'évaluer par la suite.

Un deuxième dataset [preTest.csv](./Data/preTest.csv) nous permet de tester notre modèle sur de nouvelles données et nous assurer que l'on n'avions pas fait de **sur-apprentissage**.

Enfin, nous utilisons le modèle que nous avions élaboré sur le troisième et dernier dataset [finalTest.csv](./Data/finalTest.csv) pour prédire la classe de chaque set (qui ne nous ai pas donné cette fois) et renvoyer les résultats dans un [fichier de sortie](./Data/El_Mershati_Laith_Classification.txt).


## Revue de code

Le code est composé de deux scripts, un script ["main"](./knn_El_Mershati_Laith.py) permettant de **définir les labels** d’un set de données non labelisées en s’appuyant sur une valeur précise de *k*, et un deuxième script ["Best K"](./bestK_El_Mershati_Laith.py) prenant deux datasets labelisés et **calcul le pourcentage de précision** obtenu selon chaque *k* en faisant varier les valeurs de celui-ci dans un range.

Toutefois, dû au grand nombre de données dans le dataset l’opération prend énormément de temps et on ne peut pas se permettre de tester tous les *k* allant de 1 au nombre de totales données – 1. Or, sachant qu’il n’est pas pertinent de prendre une valeur de *k* importante, on commence par évaluer les 14 premières valeurs.

![Evaluation k 1 à 14](./K/best-percentage-k-1-to-14.PNG "évaluation k 1 à 14")

Il semblerait qu’on atteint un minimum d’erreur pour **k = 8** obtenant ainsi un taux de précision de **88.33 %**. Le taux d’erreur repart ensuite à la hausse et on suppose alors qu’il ne sera pas meilleur que 8. Ce sera donc la valeur de *k* que l’on retiendra.

Afin de trouver le label d’une donnée nous allons d’abord chercher à trouver ses k plus proche voisins avec la méthode *k_selection( )*, puis déduire le label selon celui qui est le plus récurent dans la liste des k plus proche avec *getlabel( )*.

La sélection des k plus proches données se fait avec un simple calcul euclidien, cette distance est alors associée à la donnée et nous retournons les plus proches par un simple tri en prenant les k premiers.