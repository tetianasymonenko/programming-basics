seq = "ATGGATTCAATGGCCTAAACGATTGCTGATGAA"
gc = (seq.count("G") + seq.count("C")) / len(seq)

if len(seq) < 30:
    print ("too short")
elif "N" in seq:
    print ("contains unknown bases")
else:
    if gc > 0.6:
        print ("GC rich")
    elif gc < 0.4:
        print ("AT rich")
    else:
        print ("balanced")
    
    if seq.startswith("ATG") and len(seq) %3 == 0:
        print ("possible coding sequence")
    

    