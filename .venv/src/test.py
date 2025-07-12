import os,sys

def print_hi(name):
    print (f'Bonjour {name}')



if __name__ == "__main__":
    #print_hi("Blandine")
    # a = int(input("Nombre: "))    
    for a in range(1,100):
        if a%2 == 0:
            print(f'Le nombre {a} est pair')
        else:
            print(f'Le nombre {a} est impair')

print(sys.version)

