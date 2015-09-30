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

def NormalCourse(C):
  flag = False
  for i in range(len(C)):
    if C[i][0] != 0:
      flag = True
      break
  if not flag:
    print "Перший стовпчик - нульовий!"
    exit()
  count = 0
  while C[0][0] == 0:
    count += 1
    temp = C[0]
    C[0] = C[count]
    C[count] = temp
  for i in range(len(C[0])-1):    # стовпчик для "занулення"
    for j in range(i+1,len(C)):   # рядок для зміни
      M = C[j][i]/C[i][i]
      for k in range(len(C[j])):  # зміни елементів
        C[i][k] *= M
        C[j][k] -= C[i][k]
  for i in range(len(C)):
    M = C[i][i]
    for j in range(len(C[i])):
      C[i][j] /= M
  return C

def ReverseCourse(C):
  X = []
  for i in range(len(C)-1, 0-1, -1):
    S = 0
    for k in range(len(X)):
      S += X[k]*C[i][len(C)-1-k]
    X.append((C[i][len(C)] - S))
  X.reverse()
  return X

def SingleFactors():
  return ReverseCourse(NormalCourse(AttachMatrixs(InputA(), InputB())))

SingleFactors()
