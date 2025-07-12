import multiprocessing
import math


def compute_double(mylist,results,produit):
    for j,num in enumerate(mylist):
        results[j] = num*2
    
    produit.value = math.prod(results)
    print(f"Résultat (processus p1) : {results[:]}")
    print(f"Produit (processus p1) : {produit.value}")


mylist = [1, 2, 3, 4]

#ressources partagées entre les processus
results = multiprocessing.Array('i', 4)
produit = multiprocessing.Value('i')

p1 = multiprocessing.Process(target=compute_double, args=(mylist,results,produit))

p1.start()
p1.join()

print(f"Résultat (main program) : {results[:]}")
print(f"Produit (main program) : {produit.value}")
