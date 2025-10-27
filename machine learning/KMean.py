import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['Species'] = iris.target

# Step 2: Extract features (X)
X = data.iloc[:, :-1]  # All features except target

# Step 3: Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

# Step 4: Compare clusters with actual species
print("Cluster Centers:\n", kmeans.cluster_centers_)
print("\nConfusion Matrix:\n", confusion_matrix(data['Species'], data['Cluster']))
print("\nClassification Report:\n", classification_report(data['Species'], data['Cluster']))

# Step 5: Visualization
plt.figure(figsize=(8,6))
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=data['Cluster'], cmap='rainbow', s=50)
plt.title('K-Means Clustering of Iris Dataset (k=3)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()