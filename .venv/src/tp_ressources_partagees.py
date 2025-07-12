import multiprocessing


def print_records(records):
    for r in records:
        print(r)
        
def insert_record(record,records):
    print("Ajout d'un nouvel élément")
    records.append(record)
    
def remove_record(record,records):
    print("Supression d'un élément")
    for r in records:
        if r[0] == record[0] and r[1] == record[1]:
            records.remove(r)
    
if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        records = manager.list([("banane","jaune"),("citron","vert"),("orange","orange")])
        
        #insert
        new_record = ("goyave","vert")
        p1 = multiprocessing.Process(target=remove_record,args=(("citron","vert"),records,))
        
        p2 = multiprocessing.Process(target=insert_record,args=(new_record,records,))
        p3 = multiprocessing.Process(target=print_records,args=(records,))
        
        p1.start()
        p1.join()
        print (f"Après suppression : {records[:]}")

        p2.start()
        p2.join()
        
        p3.start()
        p3.join()
        