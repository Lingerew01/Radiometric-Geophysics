import matplotlib.pyplot as plt
import seaborn as sns
import data_loader


df_cleaned, Easting, Northing, Radium, Uranium, Thorium, Potasium = data_loader.load_data()
df_cleaned.columns = df_cleaned.columns.str.strip()

vars = ['D', 'Hin', 'Hex', 'ELCR']
vars2 = ['Th', 'K', 'Ra']

custom_labels = {
    'D': r'$D_{\gamma}$',
    'Hin': '$H_{in}$',
    'Hex': '$H_{ex}$',
    'ELCR': '$E_{LCR}$'
}
custom_indep_labels = {
    'Th': '$^{232}$Th',
    'K': '$^{40}K$',
    'Ra': '$^{226}$Ra'
}
def plot_regressions(ind_var):
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))

    for i, _var in enumerate(vars):
        ax = axes[i // 2, i % 2]
        sns.regplot(
            data=df_cleaned, x=ind_var, y=_var,
            scatter_kws={'s': 50, 'alpha': 0.6},
            line_kws={'color': 'red', 'linewidth': 2},
            ci=95, ax=ax
        )

        ax.set_xlabel(custom_indep_labels[ind_var], fontsize=16)
        ax.set_ylabel(custom_labels[_var], fontsize=16)

        # Grid and tick adjustments
        ax.grid(True, which='both', axis='both',
                color='gray', linestyle='--', linewidth=0.7, alpha=0.6)
        ax.tick_params(axis='both', which='major', labelsize=14)

    plt.tight_layout()
    plt.savefig(f"regression_plots_{ind_var}.png", dpi=300, bbox_inches='tight')
    plt.show()


for var2 in vars2:
    plot_regressions(var2)
