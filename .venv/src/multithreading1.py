import threading
import os

def tache1():
    print (f"tâche 1 attribuée au thread {threading.current_thread().name}")
    print (f"\tid du processus associé à la tâche 1 {os.getpid()}")

def tache2():
    print (f"tâche 2 attribuée au thread {threading.current_thread().name}")
    print (f"\tid du processus associé à la tâche 2 {os.getpid()}")
    
if __name__ == "__main__":
    print (f"id du processus associé à la tâche main {os.getpid()}")
    print (f"Nom main thread {threading.main_thread().name}")
    
    
    t1 = threading.Thread(target=tache1, name="t1") 
    t2 = threading.Thread(target=tache2, name="t2") 
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()