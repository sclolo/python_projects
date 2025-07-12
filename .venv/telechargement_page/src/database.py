import os
from os import read
from shlex import join
import mysql.connector
from mysql.connector import errorcode
from glob import glob
import re
from read_categories import readcat


class database():

    # Exemple de connexion
    # cnx = mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employees')

    # Définir des arguments de connexion dans un dictionnaire et utiliser l'opérateur ** est une autre option
    config = {
        "host": "localhost",
        "user": "root",
        "password": "1803",
        "database": "pygamon",
        # 'raise_on_warnings': True
    }

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid crédentials")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de données n'existe pas")
            else:
                print(err)
            exit()
            
    def create_table(self):
        sql = ""
        cdes = []
        cursor = self.cnx.cursor()
        flag = False
        files = glob(
            '.venv/telechargement_page/telechargements/quiz/**/*.sql', recursive=True)
        filename = files[0]
        with open(filename,'r') as f:
            content = f.read()
            commandes = content.split("\n")
            for commande in commandes:
                # print("*"*20)
                # print (commande)
                if "DROP" in commande:
                    cdes.append(commande)    
                if "CREATE" in commande:
                    flag = True
                if flag:
                    sql = sql + commande
                if flag and ";" in commande:
                    # Dans les fichiers csv le niveau est un chaine de caractères 
                    cdes.append(sql.replace('char(1)','varchar(15)'))
                    break;
            for cde in cdes:
                print (cde)
                try: 
                    if cde.rstrip() != '':
                        cursor.execute(cde)
                except mysql.connector.Error as err: 
                    print (err.msg)
                    exit()
            self.cnx.commit()
            
            
    def insert_datas(self):
        
        print("*"*20)
        print("Récupération des thèmes")
        themes = self.get_theme()
        
        print("*"*20)
        print("Lecture des données")

        commandes = []
        cursor = self.cnx.cursor()
        files = glob(
            '.venv/telechargement_page/telechargements/quiz/**/*.csv', recursive=True)
        
        for file in files:
            with open(file, 'r', encoding="utf-8-sig") as f:
                
                filename = os.path.basename(file)
                c = re.search(r"(\d+)", filename)
                theme = themes.get(c.group(0))
                
                lines = f.readlines()
                for line in lines:
                    if len(line) < 10:
                        continue
                    datas = line.replace("; "," ").split(";")
                    d = []
                    for data in datas:
                        d.append(f'"{data.replace(';','').replace('"','').replace(',','')}"')
                    if d[1] != '"fr"':
                        continue
                    #Autoincrémentation
                    d[0] = "0"
                    d.insert(2,f"'{theme}'")
                    commande = f"INSERT INTO openquizzdb VALUES ({",".join(d)})"
                    try: 
                        if commande.rstrip() != '':
                            cursor.execute(commande)
                    except mysql.connector.Error as err: 
                        print ("Il y a une erreur !")
                        print(file)
                        print (commande)
                        print (err.msg)
                        exit()
       
        self.cnx.commit()
        self.cnx.close()
        print ("C'est fini")

    def select(self):
        with self.cnx.cursor() as cursor:
            cursor.execute(
                "SELECT user, host, plugin FROM mysql.user WHERE user = 'root';")
            results = cursor.fetchall()
            print(results)
        
        self.cnx.commit()
        self.cnx.close()
        
    def get_theme(self):
        dossier_destination = "/home/stephane/python-projects/.venv/telechargement_page/telechargements/"
        return  readcat(dossier_destination, True)
        

db = database()
db.create_table()
db.insert_datas()
