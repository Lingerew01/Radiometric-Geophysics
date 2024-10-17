import pandas as pd


def load_data():
    data = pd.read_csv("Arranged_Radiation_wolaita.csv")
    coor = pd.read_csv("UTM_Coord.csv")

    New_coor = coor.drop(["X.1", "Y.1"], axis=1)
    data['Easting'] = New_coor['X']
    data['Northing'] = New_coor['Y']

    Easting = data.Easting.to_numpy()
    Northing = data.Northing.to_numpy()
    Radium = data['Ra  '].to_numpy()
    Uranium = data['U'].to_numpy()
    Thorium = data['Th  '].to_numpy()
    Potasium = data['K'].to_numpy()

    data11 = data.drop(columns=[
        ' ID',
        'Ra ',
        'Easting',
        'Northing',
        'Th/U ',
        'E',
        'I_Alpha',
        'I_Gamma'
    ])

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
    cols[a], cols[b], cols[c], cols[d], cols[e], cols[f], cols[g], cols[h], cols[i] = (
        cols[c], cols[d], cols[e], cols[a], cols[b], cols[f], cols[g], cols[h], cols[i]
    )
    df11 = data11[cols]

    df_cleaned = df11[df11['K'] < 400]

    return df_cleaned, Easting, Northing, Radium, Uranium, Thorium, Potasium

