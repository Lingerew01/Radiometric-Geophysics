import matplotlib.pyplot as plt
import seaborn as sns
import data_loader

df_cleaned, Easting, Northing, Radium, Uranium, Thorium, Potasium = data_loader.load_data()
df_cleaned.columns = df_cleaned.columns.str.strip()
df_cleaned1 = df_cleaned.drop(columns=['D', 'Hex', 'Hin', 'ELCR'])

custom_labels = {
    'Th': r'$^{232}\mathrm{Th}$',
    'K': r'$^{40}\mathrm{K}$',
    'Ra': r'$^{226}\mathrm{Ra}$',
    'U': r'$^{238}\mathrm{U}$',
    'Rn': r'$^{222}\mathrm{Rn}$'
}

sns.set_style('whitegrid')

plt.figure(figsize=(8, 6))
sns.violinplot(data=df_cleaned1)
plt.grid(True,
         which='both',
         axis='both',
         color='gray',
         linestyle='--',
         linewidth=0.7,
         alpha=0.6)
plt.xlabel("Variables", fontsize=14)
plt.ylabel("Values", fontsize=14)

plt.xticks(
    ticks=range(len(df_cleaned1.columns)),
    labels=[custom_labels.get(col, col) for col in df_cleaned1.columns],
    fontsize=12
)

plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("violin_plot_publication.png", dpi=300)
plt.show()

