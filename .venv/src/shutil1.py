import shutil

src = "src/os1.py"
dest ="src/os1copy.py"

rep = shutil.copy(src,dest)

print (rep)


