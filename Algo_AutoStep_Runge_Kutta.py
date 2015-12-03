#!/usr/bin/python
from math import *

def Diff_h_h2(x,y,f,h):
  k1=h*f(x,y); k2=h*f(x+h/2.,y+k1/2.); k3=h*f(x+h/2.,y+k2/2.); k4=h*f(x+h,y+k3); yh=y+1./6*(k1+2*k2+2*k3+k4)
  k1=h/2.*f(x,y); k2=h/2.*f(x+h/4.,y+k1/2.); k3=h/2.*f(x+h/4.,y+k2/2.); k4=h/2.*f(x+h/2.,y+k3); yh_2=y+1./6*(k1+2*k2+2*k3+k4)
  k1=h/2.*f(x+h/2.,y); k2=h/2.*f(x+h*3./4,y+k1/2.); k3=h/2.*f(x+h*3./4,y+k2/2.); k4=h/2.*f(x+h,y+k3); yh_2+=1./6*(k1+2*k2+2*k3+k4)
  return fabs(yh-yh_2)

ls = raw_input('f(x,y); x0; y0; b; eps = ').split(';')
f = lambda x,y: eval(ls[0])
x0, y0, b, eps = float(ls[1]), float(ls[2]), float(ls[3]), float(ls[4])
x,y,h = x0,y0,1.
print ' _____________________________________________ '
print '| %-20.20s | %-20.20s |' % ('x','y')
print '|----------------------+----------------------|'
while b>x:
  print '| %-20.5f | %-20.5f |' % (x,y)
  while Diff_h_h2(x,y,f,h)>eps:
    h=h/2
  while Diff_h_h2(x,y,f,h)<eps:
    h=h*2
  k1=h*f(x,y); k2=h*f(x+h/2,y+k1/2); k3=h*f(x+h/2,y+k2/2); x+=h; k4=h*f(x,y+k3); y+=1./6*(k1+2*k2+2*k3+k4)
print ' ---------------------------------------------'