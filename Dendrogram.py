
import os
import numpy as np
import pandas as pd
from scipy.interpolate import LinearNDInterpolator
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv("Arranged_Radiation_wolaita.csv")
coor = pd.read_csv("UTM_Coord.csv")
#
New_coor = coor.drop(["X.1", "Y.1"], axis=1)
#
data['Easting'] = New_coor['X']
data['Northing'] = New_coor['Y']
#
Easting = data.Easting.to_numpy()
Northing = data.Northing.to_numpy()
#
Radium = data['Ra  '].to_numpy()
Uranium = data['U'].to_numpy()
Thorium = data['Th  '].to_numpy()
Potasium = data['K'].to_numpy()

data11 = data.drop(columns=[' ID',
                            'Ra ',
                            'Easting',
                            'Northing',
                            'Th/U ',
                            'E',
                            'I_Alpha',
                            'I_Gamma'])
cols = list(data11.columns)
a, b, c, d, e, f, g, h, i = (
    cols.index('Ra  '),
    cols.index('Rn '),
    cols.index('U'),
    cols.index('Th  '),
    cols.index('K'),
    cols.index('D '),
    cols.index(' Hex '),
    cols.index('Hin '),
    cols.index(' ELCR ')
)
cols[a], cols[b], cols[c], cols[d], cols[e], cols[f], cols[g], cols[h], cols[i] = cols[c], cols[d], cols[e], cols[a], cols[b], cols[f], cols[g], cols[h], cols[i]
df11 = data11[cols]

Z = linkage(df11, method='ward')
plt.figure(figsize=(8, 6))
dendro = dendrogram(
    Z,
    labels=data11.index,
    leaf_rotation=90,
    leaf_font_size=10,
    above_threshold_color='black',
    color_threshold=0,
    distance_sort='ascending',
)

optimal_distance = 350
plt.axhline(y=optimal_distance,
            color='red',
            linestyle='--',
            linewidth=2)

optimal_clusters = fcluster(Z, optimal_distance, criterion='distance')
plt.xlabel("Samples", fontsize=14)
plt.ylabel("Euclidean Distance", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig("Dendrogram_with_Optimal_Clusters_Publication.png", dpi=300, bbox_inches="tight", pad_inches=0.1)


cluster_range = range(1, 11)
inertia = []
for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df11)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(cluster_range,inertia,'o-',
         color='blue',
         markersize=8,
         linewidth=2)

plt.xlabel("Number of Clusters", fontsize=14)
plt.ylabel("Inertia", fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)

elbow_point = 3
plt.axvline(x=elbow_point, color='red', linestyle='--', linewidth=2)
plt.text(elbow_point + 0.2, inertia[elbow_point-1] + 500, 'Optimal Number of Clusters',
         color='red', fontsize=12, weight='bold', verticalalignment='center')


plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig("Elbow_Method_Publication.png", dpi=300, bbox_inches="tight", pad_inches=0.1)
plt.show()





