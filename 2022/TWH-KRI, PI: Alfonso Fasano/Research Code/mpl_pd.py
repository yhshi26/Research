import json

import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd

# open JSON file (redacted)
r = open('redacted')

# convert JSON object to dictionary
d = json.load(r)
# print(d)

# finding what index we need
# for i in d['DiagnosticData']['LFPTrendLogs']:
#    print(i)

# convert to DataFrame
df = pd.DataFrame(d['DiagnosticData']['LFPTrendLogs'])

# print DataFrame
print(df.to_string())

# need this if running code on IDLE
# plt.show() 
