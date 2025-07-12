import multiprocessing


def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print(f"Envoi du message : {msg}")
    conn.close()


def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == 'END':
            break

        print(f"réception du message : {msg}")
        
        
if __name__ == "__main__":
    msgs = ["Salut","Lorenzo","Comment ça va ?","END"]
    
    #création du pipe
    p_conn, ch_conn = multiprocessing.Pipe()

    
    p1 = multiprocessing.Process(target=sender,args=(p_conn,msgs,))
    p2 = multiprocessing.Process(target=receiver,args=(ch_conn,))
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
