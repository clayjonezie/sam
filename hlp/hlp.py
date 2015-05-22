# high level plotting

from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import matplotlib.dates as mdates
yearsFmt = mdates.DateFormatter('%D')

# 

def number_by_time(numbers, time, filename):
  fig, ax = plt.subplots()
  ax.xaxis_date()
  ax.xaxis.set_major_formatter(yearsFmt)
  line, = plt.plot(time, numbers)
  plt.xticks(time)
  locs, labels = plt.xticks()
  plt.setp(labels, rotation=90)
  plt.gcf().subplots_adjust(bottom=0.4)
  plt.savefig(filename)


