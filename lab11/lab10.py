from sympy import *
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation,writers
import numpy as np

def midpoint(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a, b,n+1)
    
    int_aprox = 0
    for i in range(n):
        #f_mid = f((x[i]+x[i+1])/2)
        #int_aprox += f_mid
        int_aprox += (f(x[i])+f(x[i+1]))/2
        xval = [x[i],x[i+1],x[i+1],x[i]]
        #yval = [0,0,f_mid, f_mid]
        yval = [0,0,f(x[i+1]), f(x[i])]
        plt.fill(xval,yval,color="red")
    int_aprox = h*int_aprox
    return int_aprox    

def roof(x):
    return np.sqrt(1+np.cos(x)**2)

s = midpoint(roof, 0, 20, 30)

print(s)

x = np.linspace(0,20,5000)
plt.plot(x,roof(x))
plt.show()

'''
def simpson(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a, b,n+1)
    
    int_aprox = 0
    for i in range(n):
        int_aprox += (f(x[i])+4*f((x[i]+x[i+1])/2)+f(x[i+1]))/6
        xi = [x[i], (x[i]+x[i+1])/2, x[i+1]]
        yi = f(xi)
        parabola = lagrange(xi,yi)
        xval = [x[i],x[i+1]]
        xval = np.hstack(xval.sqrt(np.linspace(x[i+1],x[i],10), np.linspace(x[i+1],x[i],10)))
        yval = [0,0, parabola[np.linspace(x[i+1],x[i],10)], parabola[np.linspace(x[i+1],x[i],10)]]
        plt.fill(xval,yval,color="red")
    int_aprox = h*int_aprox
    return int_aprox    

smp = simpson(roof, 0, 20, 30)

print(smp)
'''