sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]

for seq in sequences:
    print(f"{seq} length is {len(seq)}")

length =[]
for seq in sequences:
    length.append(len(seq))
print (f"Sequeces lengths: {length}")
print (f"Average length: {sum(length)/len(length)}")

ATG_count = 0
for seq in sequences:
    if seq.startswith("ATG"):
        ATG_count = ATG_count+1
print (f"Number of sequences starting with ATG: {ATG_count}")

longer_seq = []
for seq in sequences:
    if len(seq) >5:
       longer_seq.append(seq) 
print(f"Sequences more than 5 bases: {longer_seq}")

for seq in sequences:
    count = 0
    for base in seq:
        if base == "G":
            count = count+1
        if base == "C":
            count = count +1      
    print(f"{seq} GC content is {count/len(seq)*100}")
