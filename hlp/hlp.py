# high level plotting

from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import matplotlib.dates as mdates
yearsFmt = mdates.DateFormatter('%D')

# what will this actually "return"? 
def number_to_time(numbers, time):
  fig, ax = plt.subplots()
  ax.xaxis_date()
  ax.xaxis.set_major_formatter(yearsFmt)
  line, = plt.plot(time, numbers)
  plt.xticks(time)
  locs, labels = plt.xticks()
  plt.setp(labels, rotation=90)
  plt.gcf().subplots_adjust(bottom=0.4)
  plt.savefig('foo.png')



# is called something like
number_to_time([1, 2.2, 5, 2, 1.1, 4.4, 3., 2, 9, 12, 11, 12], 
               [date.today() + timedelta(days=1),
                date.today() + timedelta(days=2),
                date.today() + timedelta(days=3),
                date.today() + timedelta(days=4),
                date.today() + timedelta(days=5),
                date.today() + timedelta(days=6),
                date.today() + timedelta(days=7),
                date.today() + timedelta(days=8),
                date.today() + timedelta(days=9),
                date.today() + timedelta(days=10),
                date.today() + timedelta(days=11),
                date.today() + timedelta(days=12)])


