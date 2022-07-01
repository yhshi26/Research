import json

import matplotlib as mpl
import matplotlib.pyplot as plt

from parser import parse, patients
from grapher import graph

with open('file_names.txt') as fn:
    file_names = fn.readlines()

for fn in file_names:
    parse(fn.split('\n')[0])

while True:
    commands = ["info", "graph", "end"]
    i = input("give command (or help) ")
    if "help" in i:
        print ("commands: " + str(commands))
    elif "info" in i:
        for p in patients:
            print(p)
    elif "graph" in i:
        for p in patients:
            graph(p)
        plt.show() 
    elif "end" in i:
        break
