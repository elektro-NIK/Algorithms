#!/usr/bin/python
# -*- coding: utf-8 -*-

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

def GausHaleckiy(A, B):
  C = []
  D = []
  Y = []
  X = []
  for i in range(len(A)):
    C.append([0]*len(A))
    D.append([0]*len(A))
  for i in range(len(A)):
    D[i][i] = 1
    D[0][i] = A[0][i] / A[0][0]
    C[i][0] = A[i][0]
  for i in range(len(A)):
    for j in range(len(A)):
      if j <= i:
        S = 0
        for k in range(j):
          S += C[i][k] * D[k][j]
        C[i][j] = A[i][j] - S
      else:
        S = 0
        for k in range(i):
          S += C[i][k] * D[k][j]
        D[i][j] = (A[i][j] - S) / C[i][i]
  for i in range(len(A)):
    S = 0
    for k in range(i):
      S += C[i][k] * Y[k]
    Y.append((B[i] - S) / C[i][i])
  for i in range(len(A)-1, -1, -1):
    S = 0
    for k in range(i+1, len(A)):
      S += D[i][k] * X[len(A)-1-k]
    X.append(Y[i] - S)
  X.reverse()
  Output(X)
  return 0

def Output(X):
  print 'Результат:'
  for i in range(len(X)):
    print 'X' + str(i+1) + ' = ' + '%.4f' % X[i]
  return 0

print "-" * 83
print 'Програма розв’язку системи рівнянь методом Гауса-Халецького.'
print 'Автор - Богдан Калінін'
print "-" * 83

GausHaleckiy(InputA(), InputB())