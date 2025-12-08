import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# PARTE 2: Importazione CSV 

df = pd.read_csv("/Users/felipegonzalezdelsolar/Desktop/vendite.csv")

print("=== Prime 5 righe ===")
print(df.head())

print("\n=== Shape (righe, colonne) ===")
print(df.shape)

print("\n=== Info dataset ===")
print(df.info())

# === PARTE 3: Elaborazioni con Pandas ===

# Aggiungere colonna incasso
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

# Incasso totale della catena
incasso_totale = df["Incasso"].sum()
print("\nIncasso totale della catena:", incasso_totale)

# Incasso medio per negozio
incasso_medio_negozio = df.groupby("Negozio")["Incasso"].mean()
print("\nIncasso medio per negozio:")
print(incasso_medio_negozio)

# 3 prodotti più venduti (per Quantità totale)
prodotti_top3 = (
    df.groupby("Prodotto")["Quantità"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
print("\nTop 3 prodotti più venduti:")
print(prodotti_top3)

# Incasso medio per negozio e prodotto
incasso_negozio_prodotto = df.groupby(["Negozio", "Prodotto"])["Incasso"].mean()
print("\nIncasso medio per Negozio & Prodotto:")
print(incasso_negozio_prodotto)

# === PARTE 4: NumPy ===

# Array Quantità
q = df["Quantità"].to_numpy()

media = np.mean(q)
minimum = np.min(q)
maximum = np.max(q)
std = np.std(q)

print("\n--- Analisi NumPy sulla Quantità ---")
print("Media:", media)
print("Minimo:", minimum)
print("Massimo:", maximum)
print("Deviazione standard:", std)

# Percentuale di vendite sopra media
percentuale = np.sum(q > media) / len(q) * 100
print("Percentuale sopra media:", percentuale, "%")

# Array 2D: Quantità + Prezzo_unitario
arr = df[["Quantità", "Prezzo_unitario"]].to_numpy()

# Calcolo incasso per ogni riga con NumPy
incasso_numpy = arr[:, 0] * arr[:, 1]

# Verifica con il DataFrame
df_check = np.allclose(incasso_numpy, df["Incasso"])
print("\nConfronto NumPy vs Pandas Incasso:", df_check)

plt.figure(figsize=(8,5))
df.groupby("Negozio")["Incasso"].sum().plot(kind="bar", color="skyblue")
plt.title("Incasso totale per negozio")
plt.xlabel("Negozio")
plt.ylabel("Incasso (€)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,7))
df.groupby("Prodotto")["Incasso"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Percentuale incassi per prodotto")
plt.ylabel("")   # rimuove l'etichetta verticale
plt.show()

df["Data"] = pd.to_datetime(df["Data"])  # conversione della data

incasso_giornaliero = df.groupby("Data")["Incasso"].sum()

plt.figure(figsize=(10,5))
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker="o")
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Data")
plt.ylabel("Incasso (€)")
plt.grid(True, alpha=0.4)
plt.tight_layout()
plt.show()

# === PARTE 6: Analisi Avanzata ===

categorie = {
    "Smartphone": "Informatica",
    "Laptop": "Informatica",
    "Tablet": "Informatica",
    "TV": "Elettrodomestici",
    "Console": "Intrattenimento",
    "Auricolari": "Accessori",
    "Smartwatch": "Accessori",
    "Monitor": "Informatica"
}

df["Categoria"] = df["Prodotto"].map(categorie)

# Incasso totale per categoria
incasso_categoria = df.groupby("Categoria")["Incasso"].sum()
print("\nIncasso totale per categoria:")
print(incasso_categoria)

# Quantità media per categoria
quantita_media_categoria = df.groupby("Categoria")["Quantità"].mean()
print("\nQuantità media per categoria:")
print(quantita_media_categoria)

# Salvataggio CSV
df.to_csv("/Users/felipegonzalezdelsolar/Desktop/vendite_analizzate.csv", index=False)
print("\nFile salvato come vendite_analizzate.csv")

plt.figure(figsize=(10,6))

plt.bar(incasso_categoria.index, incasso_categoria.values, color="lightblue", label="Incasso medio")

plt.plot(quantita_media_categoria.index, quantita_media_categoria.values, color="red", marker="o", label="Quantità media")

plt.title("Incasso medio e Quantità media per categoria")
plt.legend()
plt.tight_layout()
plt.show()

def top_n_prodotti(n):
    return df.groupby("Prodotto")["Incasso"].sum().sort_values(ascending=False).head(n)

print("\nTop 3 prodotti per incasso:")
print(top_n_prodotti(3))
