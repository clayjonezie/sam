# high level plotting

from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import matplotlib.dates as mdates
yearsFmt = mdates.DateFormatter('%d-%m-%y')

def line_number_by_time(numbers, time, xlabel=None,
                        ylabel=None, filename='out.png'):
    fig, ax = plt.subplots()
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(yearsFmt)
    #ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(mdates.AutoDateLocator))
    line, = plt.plot(time, numbers)
    plt.xticks(time)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.gcf().subplots_adjust(bottom=0.4)
    plt.savefig(filename)

def plot_number_by_time(numbers, time, xlabel=None,
                        ylabel=None, filename='out.png'):
    fig, ax = plt.subplots()
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(yearsFmt)

    ddays = 10
    datemin = min(time) - timedelta(days=ddays)
    datemax = max(time) + timedelta(days=ddays)
    valmin = min(numbers) * .95
    valmax = max(numbers) * 1.05
    ax.axis([datemin, datemax, valmin, valmax])

    line, = plt.plot(time, numbers, 'ro')
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.gcf().subplots_adjust(bottom=0.4)
    plt.savefig(filename)
