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

# redacted
# open JSON file (redacted)
r = open('redacted.json')

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

# initiate sum
sum = 0
num_data = 0

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

        # plot data on axes
        date = date_time[1].split('T')[0]
        ax.plot(date, local_field_potential, linestyle='-', marker='.', c="white")

        # add LFP to sum
        sum += local_field_potential
        num_data += 1

relative_threshold = sum/num_data
ax.axhline(y=relative_threshold, linestyle="-", c="white")

# print relative_threshold
print("Relative threshold: " + str(relative_threshold))

# need this if running code on IDLE
plt.show() 
