import json

# from IPython.display import display

import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter

import pandas as pd

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

date_form = DateFormatter("%y-%m-%d")

# (redacted)
# open JSON file (redacted)
r = open('redacted')

# can't straight-up read JSON object to a DataFrame due to ValueError: All arrays must be of same length
# df = pd.read_json('redacted')

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

# graph dark background
plt.style.use('dark_background')

# create a figure containing a single axes
fig, ax = plt.subplots() 
ax.set_title("Report graph (average local field potential values from livestream sessions)") 
ax.set_xlabel("Date")
ax.set_ylabel("Local field potential")
# set limits to number of ticks on x and y axes
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
ax.yaxis.set_major_locator(plt.MaxNLocator(11))

# traverse through DataFrame
# iterate through non-null counts of column sensing_channel and print information
for i in range(0, int(df.count())):
    # df.iloc[i] dtype: object
    # parameters: HemisphereLocationDef.Right/Left [{'DateTime', 'LFP'], name
    current = str(df.iloc[i][0][i]).split(' ')
    # parsing out parameters
    date_time = current[1].split("'")
    # year, month, day
    # date = date_time[1].split('-')
    # year = int(date[0])
    # month = int(date[1])
    # day = int(date[2].split('T')[0])]
    # hour, minute, second
    # time = date[2].split('T')[1]
    # time = time[0].split(':','Z')
    # hour = time[0]
    # minute = time[2]
    # second = time[4]
    # local field potential (LFP)
    local_field_potential = int(current[3].split(',')[0])
    # amplitude (of deep brain stimulation (DBS))
    # if (i<int(df.count())):
    #     amplitude_mA = int(current[5])
    # else:
    #     # accounting for end integer with } to parse out
    #     amplitude_mA = int(current[5].split('}')[0])
    # plot data on axes
    date = date_time[1].split('T')[0]
    ax.plot(date, local_field_potential, linestyle='-', marker='o', c="blue")

# need this if running code on IDLE
plt.show() 
