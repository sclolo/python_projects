from get_site_content import GetSiteContent

if __name__ == "__main__":

    dossier_destination = "/home/stephane/python-projects/.venv/telechargement_page/telechargements/"

    gsc = GetSiteContent()

    # gsc.get_pages_content(dossier_destination="telechargement_page/telechargements/",getonlycat=True)

    gsc.get_pages_content(dossier_destination, categories="local", overwrite=False)

    #1 sql pour avoir le format de la table 
    gsc.get_file(dossier_destination, catids=[237], extensions=["sql"],overwrite=False)
    
    gsc.get_file(dossier_destination, extensions=["csv"],overwrite=False)
