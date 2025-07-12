import os
import pytz
import re
from datetime import datetime

name = input('Entrez votre nom : ')

print("Effectuons une opération entre deux nombres")

a = input("1ère valeur: ").strip()
b = input("2nd valeur : ").strip()
op = input("opérateur (+ - * /): ").strip()

s = a + op + b
r = eval(s)

try:
    os.mkdir('hist')
except:
    print("Le dossier hist existe déjà")

os.chdir('./hist/')

with open('historique.txt', 'a+') as p:

    p.write(f'nom-utilisateur : {name}\n\n')
    p.write(f'opération : {a} {op} {b} = {r}\n\n')

    tz1 = pytz.timezone('Europe/Paris')
    dz1 = datetime.now(tz1)
    p.write(f"date et heure : {dz1.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    p.write('*****************************************************************************************\n\n')
