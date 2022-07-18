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
    # work around blank first graph error 
    # (need to fix this, will waste memory in the long-run)
    graph_hemisphere(p, p.left_diagnostic_data)
    plt.close()

    graph_hemisphere(p, p.left_diagnostic_data)
    graph_hemisphere(p, p.right_diagnostic_data)

def graph_hemisphere(p, hemisphere_diagnostic_data):
    fig, ax = plt.subplots()
    set_ax(ax) 

    sum = 0
    num_data = 0

    y_data = []

    # ax.set_title("Report graph for: " + p.first_name + " " + p.last_name) 
    for d in hemisphere_diagnostic_data:
        ax.plot(d.date, d.local_field_potential, linestyle='-', marker='.', c='white')

        sum += d.local_field_potential
        num_data += 1

        y_data.append(d.local_field_potential)

    calc(p, ax, sum, num_data, y_data)
    p.graphs.append(ax)

def set_ax(ax):
    plt.style.use('dark_background')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Local field potential')
    # set limits to number of ticks on x and y axes
    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    ax.yaxis.set_major_locator(plt.MaxNLocator(11))

def calc(p, ax, sum, num_data, y_data):
    relative_threshold = sum/num_data
    ax.axhline(y=relative_threshold, linestyle='-', c='white')

    # https://stackoverflow.com/questions/11882393/matplotlib-disregard-outliers-when-plotting
    
    # ypbot = np.percentile(y_data, 1)
    # yptop = np.percentile(y_data, 99)
    # ypad = 0.2*(yptop - ypbot)
    # y_min = ypbot - ypad
    # y_max = yptop + ypad

    # ax.set_ylim([y_min, y_max])
