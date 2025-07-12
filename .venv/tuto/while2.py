somme = 1
while somme <= 16384:
    print(f"{somme} euro(s) = {"%.2f" % round(somme  * 1.65,2)} $ canadien(s)")
    somme *= 2 
    