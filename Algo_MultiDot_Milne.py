#!/usr/bin/python
from math import *
ls = raw_input('f(x,y); x0; y0; b; h; eps = ').split(';')
f = lambda x,y: eval(ls[0])
x0, y0, b, h, eps = float(ls[1]), float(ls[2]), float(ls[3]), float(ls[4]), float(ls[5])
n = int(round((b-x0)/h))
x,y= x0,y0
print ' _____________________________________________ '
print '| %-20.20s | %-20.20s |' % ('x','y')
print '|----------------------+----------------------|'
res_y, res_f = [y], [f(x,y)]
for i in range(4):
  print '| %-20.3f | %-20.3f |' % (x,y)
  k1=h*f(x,y); k2=h*f(x+h/2,y+k1/2); k3=h*f(x+h/2,y+k2/2); x+=h; k4=h*f(x,y+k3); y+=1./6*(k1+2*k2+2*k3+k4)
  res_f.append(f(x,y))
  res_y.append(y)
for i in range(4,n+1):
  print '| %-20.3f | %-20.3f |' % (x,y)
  y_n1 = res_y[len(res_y)-1-3]+4./3*h*(2*res_f[len(res_f)-1] - res_f[len(res_f)-1-1] + 2*res_f[len(res_f)-1-2])
  y_k = res_y[len(res_y)-1-1]+1./3*h*(f(x+h, y_n1)+4*res_f[len(res_f)-1]+res_f[len(res_f)-1-1])
  while fabs(f(x+h,y_k)-f(x+h,y_n1))>eps:
    y_n1 = y_k
    y_k = res_y[len(res_y)-1-1]+1./3*h*(f(x+h, y_n1)+4*res_f[len(res_f)-1]+res_f[len(res_f)-1-1])
  res_y.append(y_n1)
  x+=h
  res_f.append(f(x,res_y[len(res_y)-1]))
print ' ---------------------------------------------'
