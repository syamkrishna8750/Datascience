import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

food = pd.read_csv("food_data.csv")

X = food[["Sweetness", "Crunchiness"]]
y = food["FoodType"]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

tomato = pd.DataFrame({"Sweetness": [4], "Crunchiness": [6]})
tomato_scaled = scaler.transform(tomato)

knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_scaled, y)

prediction = knn.predict(tomato_scaled)

print("The predicted food type of Tomato is:", prediction[0])
