import multiprocessing


def add_list(mylist, q):
    for n in mylist:
        print(f"Ajout de {n}")
        q.put(n)


def print_queue(q):
    print("Les éléments présent dans notre queue")
    while not q.empty():
        print(q.get())
    print("Notre queue est vide")


if __name__ == "__main__":
    mylist = ["toto", "tata", "popol", "lolol"]

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=add_list, args=(mylist, q,))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))
    p3 = multiprocessing.Process(target=print_queue, args=(q,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
    
    p3.start()
    p3.join()
