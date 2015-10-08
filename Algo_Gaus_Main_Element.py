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

def AttachMatrixs(A,B):
  C = []
  for i in range(len(A)):
    C.append(A[i])
    C[i].append(B[i])
  return C

def MaxElement(C):
  result = []
  temp = 0
  i = 0
  j = 0
  while temp == 0:
    temp = C[i][j]
    x = j
    y = i
    i += 1
    j += 1
  for i in range(len(C)):
    for j in range(len(C)):
      if C[i][j] > temp:
        temp = C[i][j]
        x = j
        y = i
  result.append(x)
  result.append(y)
  return result

def RemoveRowCol(C, row, col):
  C1 = C[:row]
  C2 = C[row+1:]
  Z = C1 + C2
  res = []
  for i in range(len(Z)):
    res.append(Z[i][:col]+Z[i][col+1:])
  return res

def MainElement(C):
  if len(C) == 0:
    return []
  temp = MaxElement(C)
  p = temp[1]
  q = temp[0]
  M = []
  for i in range(len(C)):
    M.append(-C[i][q]/C[p][q])
  for i in range(len(C)):
    if i != p:
      for j in range(len(C[i])):
        C[i][j] = C[i][j] + C[p][j]*M[i]
  X = MainElement(RemoveRowCol(C, p, q))
  X = X[:q] + [""] + X[q:]
  S = 0
  for i in range(len(C[p])-1):
    if i != q:
      S += X[i]*C[p][i]
  X = X[:q] + [(C[p][len(C[p])-1]-S)/C[p][q]] + X[q+1:]
  return X

def Output(X):
  for i in range(len(X)):
    print 'X' + str(i+1) + ' = ' + '%.4f' % X[i]
  return 0

print "-" * 83
print 'Програма розв’язку системи рівнянь методом Гауса з вибором головного елемента.'
print "-" * 83
Output(MainElement(AttachMatrixs(InputA(), InputB())))
