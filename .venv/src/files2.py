import os
import pytz
from datetime import datetime
import random
import glob


print("Création de x fichiers .txt")
nb = int(input("Nombre de fichiers à créer : "))

nbboucle = int(input("Boucler combien de fois ? "))

ops = ['+', '-', '*', '/']
names = ['toto', 'tata', 'popol', 'ziggy']

try:
    os.mkdir('hist')
except:
    print("Le dossier hist existe déjà")

os.chdir('./hist/')

# files = glob.glob('/home/stephane/python-projects/.venv/hist/historique*.txt')
# for file in files:
#     os.remove(file)

for nbb in range(1, nbboucle+1):
    for i in range(1, nb+1):

        a = random.randint(1, 100)
        b = random.randint(1, 100)
        op = ops[random.randint(0, 3)]
        name = names[random.randint(0, 3)]
        s = str(a) + op + str(b)
        r = eval(s)

        filename = 'historique' + str(i) + '.txt'

        with open(filename, 'a') as p:

            p.write(f'nom-utilisateur : {name}\n\n')
            p.write(f'opération : {a} {op} {b} = {r}\n\n')

            tz1 = pytz.timezone('Europe/Paris')
            dz1 = datetime.now(tz1)
            p.write(f"date et heure : {dz1.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            p.write(
                '*****************************************************************************************\n\n')
