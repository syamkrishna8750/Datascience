from scipy.odr import Model
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

x,y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

Model = KNeighborsClassifier( n_neighbors=3 )
Model.fit(X_train, y_train)

print("Accuracy:", Model.score(X_test, y_test))
