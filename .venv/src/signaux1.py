import signal
import time

def gest_alarm(signum,stack):
    
    print("\nIntercepteur : \n")
    print("Alarme : ",time.ctime())
    
#assigner gest_alarm au signal SIGALRM
signal.signal(signal.SIGALRM,gest_alarm)

#Déclencher l'alarme après 4s
signal.alarm(4)

print ("Heure actuelle", time.ctime())

#Retard suffisant pour que l'alarme apparaisse
time.sleep(6)

