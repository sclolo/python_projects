
ht = -1

while ht!=0:
    ht = float(input("Entrez le pris hors-taxe (0 pour sortir) : "))
    print ("%.2f" % round(ht * 1.2,2) if ht > 0 else "")