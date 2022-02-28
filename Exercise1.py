# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:11:29 2022

@author: niccr151
"""

from scipy import linalg
import numpy as np

#1-a,b,c,d
A = np.arange(1,10).reshape([3,3])
b = np.arange(1,4)

x = linalg.solve(A,b)
check = np.dot(A,x) - b

#1-e
C = np.arange(1,10).reshape([3,3])
D = np.random.rand(3,3)
X2 = linalg.solve(C,D)
check2 = np.dot(C,X2) - D
print('X2 =' + str(X2))

#1-f
evals, evecs = linalg.eig(A)

#1-g
Ainv = linalg.inv(A)
Ainv_det = linalg.det(Ainv)

#1-h
i = -2
while i < 3:
    if i == 0:
        i+=1
    else:
        print("Order " + str(i) + " matrix A norm:")
        print(linalg.norm(A,i))
        i+=1
