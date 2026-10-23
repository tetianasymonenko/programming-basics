def gc_content(seq):
    return round((seq.count("G")+seq.count("C"))/len(seq)*100, 2)

def reverse_complement(seq):
    return seq.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()[::-1]

def is_usable(seq, min_length=30):
    if len(seq)>min_length and "N" not in seq:
        return(True)
    else:
        return(False)

def first_atg(seq):
    atg = seq.find("ATG")
    if atg >=0:
        return(atg)
    else:
        return ("not found")

sequences =["AAAGCTATCAGCTAC", "AAAGCTATGCAGCTACCGTTGGTGCACTCTTCTTCGACGCGGCTATC", "ATGATATATGATCGCGCGGCGAATTAGCGNNNC"]

for seq in sequences:
    print (f"GC content, %:", gc_content(seq))
    print(f"Reverse complement:", reverse_complement(seq))
    print (f"Can be used for analysis:", is_usable(seq))
    print (f"First ATG position is", first_atg(seq))

    
    