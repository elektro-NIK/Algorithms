#!/usr/bin/python
from math import *
ls = raw_input('f(x,y); x0; y0; b; h = ').split(';')
f = lambda x,y: eval(ls[0])
x0, y0, b, h = float(ls[1]), float(ls[2]), float(ls[3]), float(ls[4])
n = int(round((b-x0)/h))
x,y,= x0,y0
print ' _____________________________________________ '
print '| %-20.20s | %-20.20s |' % ('x','y')
print '|----------------------+----------------------|'
for i in range(n+1):
  print '| %-20.3f | %-20.3f |' % (x,y)
  y+=h*f(x,y); x+=h;
print ' ---------------------------------------------'