mult = 1

while mult <= 20:
    nb = 7 * mult
    print(nb if nb % 3 > 0 else str(nb) + "*", end=" ")
    mult+=1
print ("\n")
