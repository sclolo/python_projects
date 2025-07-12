import multiprocessing
import os

def square(n):
    print (f"process ID pour {n}: {os.getpid()}")
    return n*n


if __name__ == "__main__":
    mylist = [1,2,3,4,5]
    
    p=multiprocessing.Pool(5)
    
    result = p.map(square,mylist)
    
    print (result)