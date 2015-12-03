#!/usr/bin/python
from math import *

def Sigma(x,y,f,h):
  k1=h/3.*f(x,y); k2=h/3.*f(x+h/3.,y+k1); k3=h/3.*f(x+h/3.,y+(k1+k2)/2); k4=h/3.*f(x+h/2.,y+3./8*k1+9./8*k3); k5=h/3*f(x+h,y+1.5*k1-4.5*k3+6*k4)
  return fabs(k1-4.5*k3+4*k4-0.5*k5)

ls = raw_input('f(x,y); x0; y0; b; eps = ').split(';')
f = lambda x,y: eval(ls[0])
x0, y0, b, eps = float(ls[1]), float(ls[2]), float(ls[3]), float(ls[4])
x,y,h = x0,y0,1.
print ' _____________________________________________ '
print '| %-20.20s | %-20.20s |' % ('x','y')
print '|----------------------+----------------------|'
while b>x:
  print '| %-20.5f | %-20.5f |' % (x,y)
  while Sigma(x,y,f,h)>5*eps:
    h=h/2
  while Sigma(x,y,f,h)<eps*5./32:
    h=h*2
  k1=h/3.*f(x,y); k2=h/3.*f(x+h/3.,y+k1); k3=h/3.*f(x+h/3.,y+(k1+k2)/2); k4=h/3.*f(x+h/2.,y+3./8*k1+9./8*k3); k5=h/3*f(x+h,y+1.5*k1-4.5*k3+6*k4)
  x+=h; y+=0.5*(k1+4*k4+k5)
print ' ---------------------------------------------'