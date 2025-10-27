import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Load dataset
food = pd.read_csv("food_data.csv")

# Step 2: Separate features and labels
X = food[["Sweetness", "Crunchiness"]]
y = food["FoodType"]

# Step 3: Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Define the test case (Tomato)
# Assume Tomato has sweetness=4, crunchiness=6
tomato = pd.DataFrame({"Sweetness": [4], "Crunchiness": [6]})
tomato_scaled = scaler.transform(tomato)

# Step 5: Train k-NN model
knn = KNeighborsClassifier(n_neighbors=3) # k=3
knn.fit(X_scaled, y)

# Step 6: Predict
prediction = knn.predict(tomato_scaled)

print("The predicted food type of Tomato is:", prediction[0])