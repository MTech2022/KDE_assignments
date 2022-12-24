import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
dataset = pd.read_csv('../data/Mall_Customers.csv')  
x = dataset.iloc[:, [3]].values 
y = dataset.iloc[:, [4]].values 

print("Displaying the scatter of x and y")
print("Close the current picture to view elbow method");
plt.scatter(x, y)
plt.show()
print("Done");

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
data = dataset.iloc[:, [3, 4]].values  
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state= 42)  
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
print("Currently displaying Elbow method picture")
plt.show()
print("Done");

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
print("n_clusters=2 scatter");
kmeans = KMeans(n_clusters=3)
print(kmeans.get_params())
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

