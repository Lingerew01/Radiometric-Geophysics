
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import data_loader

df_cleaned, Easting, Northing, Radium, Uranium, Thorium, Potasium = data_loader.load_data()
df_cleaned.columns = df_cleaned.columns.str.strip()
matrix = df_cleaned.corr().round(2)
mask = np.triu(np.ones_like(matrix, dtype=bool), k=1)
custom_labels = {
    'Ra': r'$^{226}\mathrm{Ra}$',
    'U': r'$^{238}\mathrm{U}$',
    'Th': r'$^{232}\mathrm{Th}$',
    'K': r'$^{40}\mathrm{K}$',
    'D': r'$D_{\gamma}$',
    'Hex': r'$H_{ex}$',
    'Hin': r'$H_{in}$',
    'ELCR': r'$E_{LCR}$',
    'Rn': r'$^{222}Rn$'
}

matrix = matrix.rename(index=custom_labels, columns=custom_labels)
sn.set_theme(style="white")

plt.figure(figsize=(10, 6))
sn.heatmap(matrix,
           annot=True,
           vmax=1, vmin=-1, center=0,
           cmap='vlag',
           mask=mask,
           annot_kws={"size": 10},
           cbar_kws={"shrink": 0.8})

plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
