sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)

sequneces = sequences.append("ATGCGTAGCTAG")

print(sequences)

print(f"There are {len(sequences)} sequences in the list.")
print(f"The first sequence is: {sequences[0]}")
print(f"The last sequence is: {sequences[-1]}")

sequences_length = [len(seq) for seq in sequences]
print (f"The longest sequence length is: {max(sequences_length)}")
print (f"The shortest sequence length is: {min(sequences_length)}")
print (f"The average sequence length is: {sum(sequences_length)/len(sequences_length)}")

name, chrom, start, stop = gene
print(f"Gene {name} is on {chrom} and is {stop - start} bases long")

genes = [("BRCA1", 81188), ("TP53", 25759)]
names, lengths= zip(*genes)
gene_number = names.index("TP53")
print(f"Gene {names[gene_number]} is {lengths[gene_number]} bases long")

gene[0] = "BRCA2" # TypeError: 'tuple' object does not support item assignment