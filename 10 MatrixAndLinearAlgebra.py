# Performing Matix and Linear Algebra Calculations

import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)

# Return transpose
print(m.T)

# Return Reverse

print(m.I)

#Create a vector and Multiply
v = np.matrix([[2],[3],[4]])
print(v)
print(m*v)

import numpy.linalg

#Determinant

print(numpy.linalg.det(m))

#Eigen Values
print(numpy.linalg.eigvals(m))

#solve for x in mx = v

x = numpy.linalg.solve(m,v)
print(x)

print(m*x)
print(v)