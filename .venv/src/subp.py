import subprocess
import os

with open('sortie.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)
    

os.system('cat sortie.txt')
# subprocess.run(['cat','sortie.txt'])