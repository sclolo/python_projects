from fileinput import filename
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
from time import sleep
from bs4 import BeautifulSoup
from glob import glob
import os
from slugify import slugify
from read_categories import readcat


class GetSiteContent():

    def __init__(self):

        print("*"*20)
        print("Initialisation du driver pour Chrome")

        self.download_directory = "/home/stephane/python-projects/.venv/telechargement_page/telechargements/quiz"

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")

        prefs = {"download.default_directory": self.download_directory}
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=chrome_options)

    def get_pages_content(self, dossier_destination, categories="remote", catids=[], getonlycat=False, overwrite=True):

        print("*"*20)
        print("Création des catégories")

        compteur = 1

        onecat = True if len(catids) > 0 else False

        if (categories == "remote"):
            url = "https://www.openquizzdb.org/listing/listing.php"
            self.driver.get(url)
            onclicks = self.driver.find_elements(By.CLASS_NAME, "mytt_theme")
            with open(f"{dossier_destination}categorie.txt", "w") as f:
                for o in onclicks:
                    c = re.search(r"(\d+)", o.get_attribute("onclick"))
                    f.write(f"{c.group(0)}:\"{o.text}\" \n")
                    if not onecat:
                        catids.append(c.group(0))
        elif not onecat:
            catids = readcat(dossier_destination, False)


        if not getonlycat:
            print("*"*20)
            print("Récupération des liens vers les fichiers à télécharger")
            for cid in catids:
                src = f"{dossier_destination}{cid}.txt"
                if not overwrite and os.path.isfile(src):
                    print("*"*20)
                    print(f"On passe la catégorie : {cid}")
                    continue

                with open(src, "w") as f:

                    urlcat = f"https://www.openquizzdb.org/listing/book/ajax.php?flag=2&id={cid}"
                    print(urlcat)
                    self.driver.get(urlcat)
                    self.driver.implicitly_wait(3)

                    a = BeautifulSoup(self.driver.page_source, "html.parser")
                    links = a.find_all("a")
                    for l in links:
                        href = str(l.get("href")).replace("\\", "")
                        href = href.replace("\"", "")
                        if "#" not in href:
                            # print(href)
                            f.write(href + "\r\n")

                compteur += 1
                if compteur % 10 == 0:
                    self.pause("10 récupérations")

    def get_file(self, dossier_destination, catids=None, extensions=None, overwrite=True):

        print("*"*20)
        print("Téléchargement des fichiers")
        with open(dossier_destination + "categorie.txt") as f:
            categories = dict(line.strip().split(':', 1) for line in f)

        filenames = []
        compteur = 1

        rep = dossier_destination
        if catids != None:
            for c in catids:
                filenames.append(f"{rep}{c}.txt")
        else:
            # glob('/home/stephane/python-projects/.venv/*/*.py', recursive=True)
            files = glob(rep + "*.txt")
            for f in files:
                filenames.append(f)

        urls_to_download = []
        for f in filenames:
            with open(f) as f:
                urls = f.readlines()
                if extensions != None:
                    for extension in extensions:
                        for url in urls:
                            if extension in url:
                                urls_to_download.append(url)

        # set pour ne pas avoir x fois la même url dans urls
        myset = set(urls_to_download)
        urls_to_download = list(myset)

        for url in urls_to_download:
            print("\n")
            print("*"*20)
            print(f"URL :  {url}")
            filename, src, dest = self.get_src_and_dest(
                url, categories)

            if not overwrite and not os.path.isfile(dest + "/" + filename):
                print("*"*20)
                print(f"Téléchargement du fichier : {filename}")
                self.driver.get(url)
                sleep(3)
                self.move_file(filename, src, dest)
                compteur += 1
            else:
                print("*"*20)
                print(f"On passe le fichier : {filename}")

            if compteur % 10 == 0:
                self.pause("10 téléchargements", 10)

    def move_file(self, filename, src, dest):

        # Téléchargement terminé ?
        while not os.path.isfile(src):
            sleep(1)

        if not os.path.isdir(dest):
            os.mkdir(dest)

        dest += "/" + filename

        print("*"*20)
        print(f"Renomme le fichier {filename}")
        os.rename(src, dest)

    def get_src_and_dest(self, url, categories):

        pattern = r"([a-z-]+)_*(\d+)([.a-z]{4})$"
        result = re.search(pattern, url, re.IGNORECASE)
        filename, datatype, catid = result.group(
            0), result.group(1), result.group(2)

        src = f"{self.download_directory}/{filename}"
        dest = f"{self.download_directory}/{slugify(categories[catid], separator='_')}"

        return filename, src, dest

    def pause(self, message, timer=30):
        print("*"*20)
        print(f"On attend {timer} secondes après {message}")
        sleep(timer)
