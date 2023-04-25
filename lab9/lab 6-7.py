

from sympy import Symbol, diff, lambdify
import numpy as np
from scipy.optimize import fsolve
from time import perf_counter

def coarda_er(f, a, b, er, x0=None):
    x=Symbol('x')
    f2=diff(f,x,2)
    f2=lambdify(x,f2)
    f=lambdify(x,f)
    r_ex=fsolve(f, (a+b)/2)
    print(r_ex)
    if f(a) * f2(a) < 0:
        x=a
        while abs(r_ex-x)>er:
            x=x-f(x)/(f(x)-f(b))*(x-b)
    else:
        x=b
        while abs(r_ex-x)>er:
            x=x-f(x)/(f(x)-f(a))*(x-a)
    return x


def coarda_itr(f, a, b, er, n,x0=None):
    x=Symbol('x')
    f2=diff(f,x,2)
    f2=lambdify(x,f2)
    f=lambdify(x,f)
    r_ex=fsolve(f, (a+b)/2)
    print(r_ex)
    if f(a) * f2(a) < 0:
        x=a
        for i in range(n):
            x=x-f(x)/(f(x)-f(b))*(x-b)
    else:
        x=b
        for i in range(n):
            x=x-f(x)/(f(x)-f(a))*(x-a)
    return x
            
fs='sin(x)'
a=2
b=4
t0_coarda_er=perf_counter()   
r_aprox = coarda_er(fs, a,b,10**-3)
t1_coarda_er=perf_counter()
print(r_aprox)
t_final=t1_coarda_er - t0_coarda_er
print(t_final)
r_iter = coarda_er(fs,a,b,10**-3, 20)
print(r_iter)

def tangenta_er(f, a, b, er, x0=None):
    if x0 == None:
        x0=np.random.rand() * (b-a)+a
        x=Symbol('x')
        f1= diff(f,x)
        f=lambdify(x,f); f1=lambdify(x,f1)
        while f(x0)*f1(x0) < 0:
            x0=np.random.rand() * (b-a)+a
        r_ex=fsolve(f,x0)
        while abs(r_ex-x)>0:
            x=x-f(x)/f1(x)
    return x

t0_coarda_er=perf_counter()   
r_aprox = coarda_er(fs, a,b,10**-3)
t1_coarda_er=perf_counter()
print(r_aprox)
t_final=t1_coarda_er - t0_coarda_er
print(t_final)

def contractie_er(g,a,b,er,x0=None):
    if x0 == None:
        x0=(a+b)/2
        f=g+'-x'
        x=Symbol('x')
        f=lambdify(x,f); g=lambdify(x,g)
        r_ex=fsolve(f,x0)
        x=x0
        while abs(r_ex-x)>er:
            x=g(x)
    return x

r_aprox=contractie_er('0.5*(x+11/x)', np.sqrt(11), 30, 10**-3)
print(r_aprox)
    
        

                