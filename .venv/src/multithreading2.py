from concurrent.futures import ThreadPoolExecutor
import math

values = [3,4,5,6]

def cube(x):
    print(f"Cube de {x} : {round(math.pow(x,3))}")
    
    
if __name__ == "__main__":
    
    results=[]
    with ThreadPoolExecutor(max_workers=5) as exe:
        #appelle 1 fois cube
        exe.submit(cube,2)
        
        results = exe.map(cube,values)
        
    for r in results:
        print (r)