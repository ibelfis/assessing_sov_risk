#Importation des modules nécessaires
import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
#importation du dataset Iris
iris= load_iris()
#Déclaration de l'arbre de décision
clf = DecisionTreeClassifier(max_depth=3)
#Entrainement de l'abre de décision 
clf.fit(iris.data, iris.target)
#Affichage de l'abre de décision obtenu après entraînement

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
plt.show()
