from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Load the Iris dataset (a classic dataset included in scikit-learn)
iris = load_iris()
X = iris.data
y = iris.target

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier to the data
clf.fit(X, y)

# Visualize the decision tree rules (text representation)
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Decision Tree Rules:\n", tree_rules)
