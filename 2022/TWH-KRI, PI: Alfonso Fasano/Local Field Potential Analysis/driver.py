import json

import matplotlib as mpl
import matplotlib.pyplot as plt

from parser import parse, patients
from grapher import graph

with open('file_names.txt') as fn:
    file_names = fn.readlines()

# file_names stored locally to protect any potential sensitive information
for fn in file_names:
    parse(fn.split('\n')[0])

for p in patients:
    graph(p)

while True:
    i = input("give command (options: info, graph, end) ")
    if "info" in i:
        for p in patients:
            print(p)
    elif "graph" in i:
        plt.show() 
    elif "end" in i:
        break
