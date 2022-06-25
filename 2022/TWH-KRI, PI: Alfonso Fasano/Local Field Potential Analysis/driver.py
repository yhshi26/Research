import json

import matplotlib as mpl
import matplotlib.pyplot as plt

from parser import parse, patients
from grapher import graph

# open file_names.txt as fn 
# read fn lines and store as array of str values
with open('file_names.txt') as fn:
    file_names = fn.readlines()

# iterate through fn in file_names, call parser with fn as argument
# file_names stored locally to protect any potential sensitive information
for fn in file_names:
    parse(fn.split('\n')[0])

for p in patients:
    graph(p)

while True:
    i = input("give command (options: info, graph) ")
    if "info" in i:
        for p in patients:
            print(p)
    elif "graph" in i:
        # need this if running code on IDLE
        plt.show() 
