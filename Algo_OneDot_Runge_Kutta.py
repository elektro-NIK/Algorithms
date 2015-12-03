#!/usr/bin/python
from math import *
ls = raw_input('f(x,y); x0; y0; b; h = ').split(';')
f = lambda x,y: eval(ls[0])
x0, y0, b, h = float(ls[1]), float(ls[2]), float(ls[3]), float(ls[4])
n = int(round((b-x0)/h))
x,y= x0,y0
print ' _____________________________________________ '
print '| %-20.20s | %-20.20s |' % ('x','y')
print '|----------------------+----------------------|'
for i in range(n+1):
  print '| %-20.3f | %-20.3f |' % (x,y)
  k1=h*f(x,y); k2=h*f(x+h/2,y+k1/2); k3=h*f(x+h/2,y+k2/2); x+=h; k4=h*f(x,y+k3); y+=1./6*(k1+2*k2+2*k3+k4)
print ' ---------------------------------------------'
