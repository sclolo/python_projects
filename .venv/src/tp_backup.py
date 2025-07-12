from multiprocessing import Manager, Process, Queue
import glob
import time
from datetime import datetime
from zipfile import ZipFile
from ctypes import c_char_p


def read_dir(path, q, files):

    print(f"Début de la lecture du répertoire {path}")
    time.sleep(1)
    nbdirs = len(glob.glob(path + "**/*/", recursive=True))
    nbfiles = len(glob.glob(path + "**/*.*", recursive=True))
    for f in glob.glob(path + "**/*.txt", recursive=True):
        files.append(f)
    nbtxt = len(files)
    q.put(f'Nombre de sous répertoires : {nbdirs}')
    q.put(f'Nombre de fichiers txt : {nbtxt}')
    q.put(f'Nombre de fichiers autres : {nbfiles - nbtxt}')


def create_zipfile(files, zipfilename):
    print(f"Création de l'archive {zipfilename.value}")
    time.sleep(1)
    d1 = datetime.now()
    q.put(f'Date du dernier backup : {d1.strftime(" le %d/%m/%Y à %H:%M:%S")}')
    zipfilename.value = "backup_" + d1.strftime("%d_%m_%Y-%H_%M_%S") + ".zip"
    with ZipFile(zipfilename.value, 'a') as zipfile:
        for f in files:
            zipfile.write(f)


def read_zipinfos(zipfilename):
    print("Contenu de l'archive : ")
    time.sleep(1)
    with ZipFile(zipfilename, 'r') as zip:
        for info in zip.infolist():
            print(f"\t Fichier : {info.filename} Taille : {info.file_size}")


def dump_queue(q):
    print("Lecture de file d'attente")
    print("*"*70)
    time.sleep(1)
    while not q.empty():
        print(q.get())


if __name__ == "__main__":

    manager = Manager()
    files = Manager().list()
    zipfilename = Manager().Value(c_char_p, "")

    q = Queue()
    path = "/home/stephane/python-projects/.venv/hist/"

    q.put(f'Informations sur le dossier : {path}')

    p1 = Process(target=read_dir, args=(path, q, files,))
    p1.start()
    p1.join()

    p2 = Process(target=create_zipfile, args=(files, zipfilename))
    p2.start()
    p2.join()

    p3 = Process(target=dump_queue, args=(q,))
    p3.start()
    p3.join()

    p4 = Process(target=read_zipinfos, args=(zipfilename.value,))
    p4.start()
    p4.join()
