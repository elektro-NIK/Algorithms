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
  for it in range(len(C)):                  # main element
    for i in range(len(C)):                 # run on all rows
      if i != it:
        M = C[i][it] / C[it][it]
        for j in range(len(C[i])):
          C[it][j] *= M
          C[i][j] -= C[it][j]
  for i in range(len(C)):
    C[i][len(C)] /= C[i][i]
    C[i][i] = 1.0
  return C

def ReverseCourse(C):
  X = []
  for i in range(len(C)):
    X.append(C[i][len(C)])
  return X

def GausJordan():
  return ReverseCourse(NormalCourse(AttachMatrixs(InputA(), InputB())))

print GausJordan()
