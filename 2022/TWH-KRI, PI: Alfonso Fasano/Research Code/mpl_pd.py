import json

# from IPython.display import display

import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd

# (redacted)
# open JSON file (redacted)
r = open('redacted')

# can't straight-up read JSON object to a DataFrame due to ValueError: All arrays must be of same length
# df = pd.read_json('Report_Json_Session_Report_20220607T123815[1].json')

# to combat this we convert the JSON object to a dictionary before converting it to a DataFrame, giving us control
d = json.load(r)

# indexing through the dictionary to find what index we need
# for i in d['DiagnosticData']['LFPTrendLogs']:
#    print(i)

# converting the dictionary to a DataFrame using the indexes we need
df = pd.DataFrame(d['DiagnosticData']['LFPTrendLogs'])

# get information on df
df.info()

# traverse and print DataFrame
# iterates over sensing_channel only due to DataFrame form (I think)
for i in df:
    sensing_channel = i

# finding range to tranverse through DataFrame
# print("df.count() to int: " + str(df.count()))

# traverse through DataFrame
# iterate through non-null counts of column sensing_channel and print information
for i in range(0, int(df.count())):
    print(df.iloc[i])

# need this if running code on IDLE
# plt.show() 
