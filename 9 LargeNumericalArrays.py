# Calculating with Large Numerical Arrays

# Python Lists

x = [1,2,3,4]
y = [6,7,8,9]
print(x*2)
print(x+y)

import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax*2)
print(ax+10)
print(ax+ay)
print(ax*ay)

def f(x):
    return 3*x**2 - 2*x+7

print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(10000,10000),dtype=float)
print(grid)

print(grid+10)
c = np.sin(grid)
print(c)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)

# Select row 1

print(a[1])

#Select Column 1
print(a[:,1])

#Select a subregion and change it
print(a[1:3,1:3])

#Broadcast a row vector across an operation on all rows
print(a+[100,101,102,103])
print(a)
# Conditional Assignment on an Array
print(np.where(a < 10, a, 10))