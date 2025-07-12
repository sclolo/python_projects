
def readcat(dossier_destination, with_titles):
    catids = []
    themes = {}
    with open(f"{dossier_destination}categorie.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            a = line.replace("\n", "").replace('"', '').strip().split(':')
            if with_titles:
                themes[a[0]] = a[1]
            else:
                catids.append(a[0])
    if with_titles:
        return themes
    else:
        return catids
