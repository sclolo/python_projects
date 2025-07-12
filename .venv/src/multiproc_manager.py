# Ajout d'un élément dans une liste en utilisant le processus serveur

import multiprocessing

def print_records(records):
    for record in records:
        print(f"Nom: {record[0]}\nScore: {record[1]}")
        
def insert_record(record,records):
    print("Ajout d'un nouvel élément")
    records.append(record)
    
    
if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        records = manager.list([('Popol',20),("toto",10),("lolo",40)])
        
        print("Avant insertion")
        print_records(records)
        
        #insert
        new_record = ("Ali",5)
        
        p1 = multiprocessing.Process(target=insert_record,args=(new_record,records,))
        p2 = multiprocessing.Process(target=print_records,args=(records,))
        
        p1.start()
        p1.join()
        
        print("Après insertion")
        p2.start()
        p2.join()
    
