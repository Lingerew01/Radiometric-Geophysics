import os
import numpy as np
import pandas as pd
from scipy.interpolate import LinearNDInterpolator
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import verde as vd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


data = pd.read_csv("Arranged_Radiation_wolaita.csv")
coor = pd.read_csv("UTM_Coord.csv")
#
New_coor = coor.drop(["X.1", "Y.1"], axis  =  1)
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

#
# Define the list of data elements and labels
l = [Radium, Uranium, Thorium, Potasium]
custom_labels = [
    r'$^{226}\mathrm{Ra} \ \mathrm{Bqkg}^{-1}$',
    r'$^{238}\mathrm{U} \ \mathrm{Bqkg}^{-1}$',
    r'$^{232}\mathrm{Th} \ \mathrm{Bqkg}^{-1}$',
    r'$^{40}\mathrm{K} \ \mathrm{Bqkg}^{-1}$'

]
#
fig, axs = plt.subplots(2, 2, figsize=(6, 8))
for i, element in enumerate(l):
    ax = axs[i // 2, i % 2]

    reducer = vd.BlockReduce(np.median, spacing=10)
    block_coords, block_intensity = reducer.filter((Easting, Northing), element)

    spline = vd.Spline()
    spline.fit(block_coords, block_intensity)

    grid = spline.grid(spacing=40,
                       data_names='Intensity')
    grid = vd.distance_mask((Easting, Northing),
                            maxdist=250,
                            grid=grid)

    img = grid.Intensity.plot(
        ax=ax,
        cmap='viridis',
        robust=True,
        vmin=0,
        add_colorbar=False)

    ax.axis('scaled')

    ax.set_xlabel('Easting [m]', fontsize=12)
    ax.set_ylabel('Northing [m]', fontsize=12)

    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2000))

    cbar = plt.colorbar(img, ax=ax)
    cbar.set_label(str(custom_labels[i]), fontsize=10)

fig.tight_layout(w_pad=3.08)
plt.savefig('subplots_grid.png', dpi=300, bbox_inches='tight')
plt.show()
