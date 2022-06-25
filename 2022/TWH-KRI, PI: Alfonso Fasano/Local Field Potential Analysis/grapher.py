import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter

import numpy as np
import pandas as pd

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from patient import *

def graph(p): 
    # create a figure containing a single axes
    fig, ax = plt.subplots()
    set_ax(ax) 

    # initiate sum
    sum = 0
    num_data = 0

    y_data = []

    ax.set_title("Report graph for: " + p.first_name + " " + p.last_name) 
    for d in p.diagnostic_data:
        ax.plot(d.date, d.local_field_potential, linestyle='-', marker='.', c="white")

        # add LFP to sum
        sum += d.local_field_potential
        num_data += 1

        y_data.append(d.local_field_potential)

    calc(p, ax, sum, num_data, y_data)
    p.set_graph(ax)

def set_ax(ax):
    # graph dark background
    plt.style.use('dark_background')
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Local field potential")
    # set limits to number of ticks on x and y axes
    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax.yaxis.set_major_locator(plt.MaxNLocator(11))

def calc(p, ax, sum, num_data, y_data):
    relative_threshold = sum/num_data
    ax.axhline(y=relative_threshold, linestyle="-", c="white")

    # finding limits for y-axis (https://stackoverflow.com/questions/11882393/matplotlib-disregard-outliers-when-plotting)    
    ypbot = np.percentile(y_data, 1)
    # change yptop percentile to be higher/lower depending on fruequency or extremity of outliers in data
    # yptop = np.percentile(y_data, 75)
    yptop = np.percentile(y_data, 99)
    ypad = 0.2*(yptop - ypbot)
    y_min = ypbot - ypad
    y_max = yptop + ypad

    ax.set_ylim([y_min, y_max])
