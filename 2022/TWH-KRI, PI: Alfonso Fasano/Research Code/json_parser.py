import json

# from IPython.display import display

import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter

import numpy as np
import pandas as pd

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

date_form = DateFormatter("%y-%m-%d")

# redacted
# open JSON file (redacted)
r = open('redacted')

# can't straight-up read JSON object to a DataFrame due to ValueError: All arrays must be of same length
# df = pd.read_json('redacted')

# to combat this we convert the JSON object to a dictionary before converting it to a DataFrame, giving us control
d = json.load(r)

# converting the dictionary to a DataFrame using the indices we need
df = pd.DataFrame(d['DiagnosticData']['LFPTrendLogs'])

# get information on df
# df.info()

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

y_data = []

# traverse through DataFrame
# iterate through non-null counts of column sensing_channel and print information
for i in range(0, int(df.count())):
    # df.iloc[i] dtype: object
    # parameters: HemisphereLocationDef.Right/Left [{'DateTime', 'LFP'], name
    session = df.iloc[i][0]
    for i in range(0, int(len(session))):
        current = str(session[i]).split(' ')
        # parsing out parameters
        date_time = current[1].split("'")
        # local field potential (LFP)
        local_field_potential = int(current[3].split(',')[0])
        y_data.append(local_field_potential)

        # plot data on axes
        date_time = date_time[1].split('T')
        date = date_time[0]
        time = date_time[1].split('Z')[0].split(':')
        date_time = str(date) + "-" + str(time[0]) + "-" + str(time[1]) + "-" + str(time[2])
        ax.plot(date_time, local_field_potential, linestyle='-', marker='.', c="white")

# finding limits for y-axis (https://stackoverflow.com/questions/11882393/matplotlib-disregard-outliers-when-plotting)    
ypbot = np.percentile(y_data, 1)
yptop = np.percentile(y_data, 99)
ypad = 0.2*(yptop - ypbot)
y_min = ypbot - ypad
y_max = yptop + ypad

ax.set_ylim([y_min, y_max])

# need this if running code on IDLE
plt.show() 
