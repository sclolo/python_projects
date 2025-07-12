import signal
import sys

def signal_handler(sig,frame):
    print ("\nVous avez appuyer sur ctrl-c")
    sys.exit(0)
    
signal.signal(signal.SIGINT,signal_handler)
    
print ("Appuyez sur ctrl-c")
signal.pause()