import json

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

# try opening JSON file (redacted)
f = open('redacted.json')

# return JSON object as a dictionary
data = json.load(f)

# iterate through JSON list (redacted)
for i in data["redacted"]:
    print(i)

f.close()

# need this if running code on IDLE
# plt.show() 
