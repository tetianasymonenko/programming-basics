import pandas as pd
df = pd.read_csv("data/samples.csv")
print(f"Columns: {df.columns.tolist()}")
print(f"Sample count: {df['sample'].count()}")
print(f"Average length: {df['length'].mean().__round__(2)}")
print(f"Unique organisms: {df['organism'].unique()}")
print(f"Escherichia coli samples: \n {df[df['organism'] == 'Escherichia coli']}")
print(f"Samples with length > 1000 and GC content > 42: \n {df[(df['length'] > 1000) & (df['gc_content'] > 42)]}")
print(f"Top 3 samples by GC content: \n {df.sort_values(by='gc_content', ascending=False).head(3)}")
df["length_kb"] = df["length"] / 1000
print(f"First 3 samples with length in KB: \n {df[['length_kb']].head(3)}")
print(f"Organism counts: \n {df['organism'].value_counts()}")