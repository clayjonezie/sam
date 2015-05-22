from datetime import time
from hlp import hlp

def graph(ycol, xcol):
  filename = "/home/sam/static/imgs/foo.png"
  hlp.number_by_time(ycol, xcol, filename)
