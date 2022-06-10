import json

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

# try opening JSON file (redacted)
report = open('redacted')

# return JSON object as a dictionary
# datadict = json.load(report)
# print(datadict)
datanp = np.array(json.load(report))
print(datanp)

# iterate through JSON list (redacted)
for i in datanp['redacted']:
    print(i)

report.close()

# need this if running code on IDLE
# plt.show() 
