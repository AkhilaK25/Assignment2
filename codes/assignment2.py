"""Akhila k
CS21BTECH11031"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x = sp.symbols('x')
y = sp.exp(sp.atan(x))
dif1= sp.diff(y,x)
dif2=sp.diff(y,x,2)
print(dif1)
print(dif2)
if ((1+x**2)*dif2==-1*(2*x-1)*dif1):
  #i.e., (1+x**2)*dif2+(2*x-1)*dif1==0
  print("hence proved")

#plotting the graph 
x = np.arange(-1,1,0.001)
y = np.exp(np.arctan(x))
plt.plot(x , y, color = 'b', label = 'y = exp(arctan(x))')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.legend(loc = 'upper left')
plt.show()
