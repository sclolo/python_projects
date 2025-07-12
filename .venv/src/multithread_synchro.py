from ast import main
import threading
import time

# Variable globale


def increment():
    global x
    x += 1


def thread_tache(lock):
    time.sleep(1)
    lock.acquire()  
    for _ in range(100000):
        increment()

    lock.release()

def main_tache():
    global x
    x = 0
    
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_tache,args=(lock,))
    t2 = threading.Thread(target=thread_tache,args=(lock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    for i in range(10):
        main_tache()
        print (f"Itération {i}: x = {x}")
