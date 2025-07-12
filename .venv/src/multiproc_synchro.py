import multiprocessing

def double(nbr,lock):
    print ("p1 starts")
    lock.acquire()
    nbr.value *= 2
  
    print ("p1 stops")
    lock.release()

def carre(nbr,lock):
    print ("p2 starts")
    lock.acquire()
    nbr.value *= nbr.value
    print ("p2 stops")
    lock.release()

def main():
    #init nbr dans la mémoire partagée par les processus
    nombre = multiprocessing.Value('i',2)
    
    #verrou
    lock = multiprocessing.Lock()
    
    #processus
    p1 = multiprocessing.Process(target=double,args=(nombre,lock))
    p2 = multiprocessing.Process(target=carre,args=(nombre,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print (f"Resultat : {nombre.value}")
    
if __name__ ==  "__main__":
    main()