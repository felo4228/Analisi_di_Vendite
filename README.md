# Retail Sales Analysis – Electronics Store Chain

Overview

This project simulates a real-world analytics workflow for a chain of electronics stores.  
The goal is to analyze daily sales data in order to:

- understand store performance
- study product trends
- monitor revenue over time
- explore categories and customer demand patterns

The project is built in **Python** using:

- **Pandas** for data loading and analysis  
- **NumPy** for fast numerical computations  
- **Matplotlib** for data visualization  

The dataset is stored in a CSV file called `vendite.csv`.


## 📂 Dataset

The main dataset (`vendite.csv`) contains at least 30 rows with the following columns:

- `Data` – Date of the sale (format: `YYYY-MM-DD`)
- `Negozio` – Store name (e.g., *Milano, Roma, Napoli, Torino, Bologna…*)
- `Prodotto` – Product name (e.g., *Smartphone, Laptop, TV, Tablet, Console…*)
- `Quantità` – Quantity sold (integer)
- `Prezzo_unitario` – Unit price (float)

Example row:

```text
2023-09-01,Milano,Smartphone,5,499.99
