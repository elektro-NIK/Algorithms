#!/usr/bin/python
# -*- coding: utf-8 -*-

def InputA():
  order = int(raw_input('Введіть порядок матриці: '))
  print "Матриця:"
  A = []
  for i in range(order):
    row = raw_input().split()
    for j in range(len(row)):
      row[j] = float(row[j])
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

def Minor(A, x, y):
  A = A[:y] + A[y+1:]
  for i in range(len(A)):
    A[i] = A[i][:x] + A[i][x+1:]
  return A

def DetMatrix(A):
  det = 0
  if len(A) == 2:
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
  else:
    for i in range(len(A)):
      det += (-1)**i*A[0][i]*DetMatrix(Minor(A, i, 0))
  return det

def ReplCol(A, B, x):
  for i in range(len(A)):
    A1 = A[i][:x]
    A1.append(B[i])
    A2 = A[i][x+1:]
    for j in A2:
      A1.append(j)
    A[i] = A1[:]
  return A

def Cramer():
  A = InputA()
  B = InputB()
  C = A[:]
  D = []
  det = DetMatrix(A)
  if det == 0:
    print "Детермінант дорівнює 0!"
    exit()
  for i in range(len(A)):
    A = C[:]
    D.append(DetMatrix(ReplCol(A,B,i)))
  X = []
  for i in range(len(D)):
    X.append(D[i]/det)
  return X

def Output(X):
  for i in range(len(X)):
    print 'X' + str(i+1) + ' = ' + '%.4f' % X[i]
  return 0

print "-" * 83
print 'Програма розв’язку системи рівнянь методом Крамера.'
print "-" * 83
Output(Cramer())
