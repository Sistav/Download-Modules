from os import system
import sys
import os

from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from typing import Counter



filename = sys.argv[1:]

if not filename:
    Tk().withdraw()
    filename = askopenfilename()
l = []
print(filename)
with open(filename,'r',encoding='utf-8') as file:   
    for line in file:    
        for word in line.split():
            l.append(word)
            
imports = []

for i in range(len(l)):
    if l[i] == "import" or l[i] == "from":
        imports.append(l[i+1])

for i in range(len(imports)):
    if "." in imports[i]:
        imports[i] = imports[i][:(imports[i].find("."))]

print(imports)
for i in imports:
    os.system(f"python -m pip install {i}")