import time
import multiprocessing
import os

def exemple(s):
    print(f"{s} sec de repos")
    time.sleep(s)
    print("fin du repos")
    
print(f"p : {os.getpid()}")
    
start = time.perf_counter()
    
p1 = multiprocessing.Process(target=exemple, args=(2,))
p2 = multiprocessing.Process(target=exemple, args=(4,))

p1.start()
p2.start()

print(f"p1 : {p1.pid}")
print(f"p2 : {p2.pid}")

#Attend que les processus soient terminés
p1.join()
p2.join()
    
fin = time.perf_counter()

print(f"terminée en {round(fin-start,2)} secondes")