import os, glob

# os.system('ping 127.0.0.1')
os.system('clear')
files = glob.glob('/home/stephane/python-projects/.venv/*/*.py', recursive=True)

for f in files:
    print(f)    