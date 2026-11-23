import pandas as pd
import requests


genes = ["BRCA1", "BRCA2", "TP53", "EGFR", "MYC", "KRAS", "CFTR", "HBB"]
rows = []

for symbol in genes:
    url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{symbol}"   
    response = requests.get(url, headers={"Content-Type": "application/json"})
    response.raise_for_status()      
    gene = response.json()           
    rows.append({"gene": symbol, "chromosome": gene["seq_region_name"], "length": gene["end"] - gene["start"] + 1})

df = pd.DataFrame(rows)
df.to_csv("~/kse/programming-basics/results/genes.csv", index=False) 