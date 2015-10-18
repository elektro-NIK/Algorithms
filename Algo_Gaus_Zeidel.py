#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

eps = 0.00001

def InputA():
  order = int(raw_input('Введіть порядок матриці: '))
  print "Матриця:"
  A = []
  for i in range(order):
    row = raw_input().split()
    for i in range(len(row)):
      row[i] = float(row[i])
    A.append(row)
  for i in range(order):
    if len(A[i]) != order:
      print "Матриця не вірна!"
      exit()
  return A

def InputB():
  B = raw_input('Введіть рядок вільних членів: ').split()
  for i in range(len(B)):
    B[i] = float(B[i])
  return B

def Output(X):
  print 'Результат:'
  for i in range(len(X)):
    print 'X' + str(i+1) + ' = ' + '%.4f' % X[i]
  return 0

def FirstNorme(A):
  tepm = []
  for i in range(len(A)):
    S = 0
    for j in range(len(A)):
      S += math.fabs(float(A[i][j]))
    tepm.append(S)
  return max(tepm)

def SecondNorme(A):
  tepm = []
  for i in range(len(A)):
    S = 0
    for j in range(len(A)):
      S += math.fabs(A[j][i])
    temp.append(S)
  return max(temp)

def ThirdNorme(A):
  S = 0
  for i in range(len(A)):
    for j in range(len(A)):
      S += math.fabs(A[i][j])**2
  return math.sqrt(S)

def Convergency(A):
  result = False
  if FirstNorme(A) < 1 or SecondNorme(A) < 1 or ThirdNorme(A) < 1:
    result = True
  return result

def ConvertMatrix(A,B):
  for i in range(len(A)):
    main = A[i][i]
    for j in range(len(A)):
      A[i][j] /= -main
    B[i] /= main
    A[i][i] = 0.0
  return A, B

def Compare(oldX, newX):
  res = True
  for i in range(len(oldX)):
    if math.fabs(oldX[i] - newX[i]) > eps:
      res = False
  return res

def CalculateX(A, B, X):
  newX = []
  for i in range(len(A)):
    S = 0
    for j in range(len(A)):
      if j < len(newX):
        S += newX[j]*A[i][j]
      else:
        S += X[j]*A[i][j]
    newX.append(B[i] + S)
  return newX

def Solve(A,B):
  C = ConvertMatrix(A,B)
  A = C[0]
  B = C[1]
  n = 0
  oldX = [1]*len(A)
  newX = [0]*len(A)
  if Convergency(A):
    while not Compare(oldX, newX):
      oldX = newX[:]
      newX = CalculateX(A, B, oldX)
      n += 1
    print "Ітерація №" + str(n)
    Output(newX)
  else:
    print "Система не збіжна!"
    exit()

def Zeidel():
  print "-" * 83
  print 'Програма розв’язку системи рівнянь методом Гауса-Зейделя.'
  print "-" * 83
  Solve(InputA(), InputB())

Zeidel()