import pandas as pd

df = pd.read_excel(r'dane\samochody.xlsx',sheet_name="dane")

# print (df.head(10).to_string())

# df2 = pd.read_csv(r'dane\dane_2_mln.csv',sep=";",encoding="utf-8-sig")

# print (df2.head(10).to_string())

print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

nazwy = df['Marka'].unique()
print(nazwy)

drogie_pojazdy = df[df['Cena_PLN'] > 100000]
print(drogie_pojazdy)

kolumny = ['Kolor', 'Cena_PLN','Marka']

filtr =  df["Kolor"].isin(['Czerwony','Biały','Różowy'])  \
    & ( df["Cena_PLN"] <= 50000 )

df_filtr = df.loc[filtr,kolumny].sort_values(["Cena_PLN"],ascending=[True])
print(df_filtr)

wynik = df[df.isna().any(axis=1)]  # szukanie po wierszach axis = 1
print(wynik)

df["Cena_brutto"] = df['Cena_PLN'] * 1.23
print(df)

