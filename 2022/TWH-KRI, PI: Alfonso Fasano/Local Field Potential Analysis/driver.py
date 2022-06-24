import json
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
