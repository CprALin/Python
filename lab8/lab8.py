'''
   Ex_1:

   x0 = 1 => c1 * 1/3**0 + c2 * 3**0 = c1 + c2 = 1 => c2 = 1 - c*1
   
   x1 = 1/3 =>c1 * 1/3**1 + c2 * 3**1 = c1 * 1/3 + 3c2 = 1/3 => c1 * 1/3 + 3(1-c1) = 1/3 => (-8/3)c1 = -8/3 => c1 = 1 | c2 = 0

''' 
print("Ex_1:")
print()
xn_2 = 1
xn_1 = 1/3
c1 = 1
c2 = 0

for n in range (2,11):
    xn = 10/3 * xn_1 - xn_2
    xn_exact = c1 * 1/3**n +c2 * 3 ** n
    er_n = abs(xn_exact - xn)
    xn_2 = xn_1
    xn_1 = xn
    print(er_n)
    
    if n>=3:
        rap_n = er_n/er_n_1
        print(rap_n)
    er_n_1 = er_n     

 #crestere exponentiala , foarte ineficienta

print()

#Ex_2
print("Ex_2:")
print()
xn_2 = 1
xn_1 = 1/3
c1 = 1
c2 = -2/3

for n in range (2,11):
    xn = 2 * xn_1 - xn_2
    xn_exact = c1  + c2 * n
    er_n = abs(xn_exact - xn)
    xn_2 = xn_1
    xn_1 = xn
    print(er_n)
    
    if n>=3:
        dif_n = er_n - er_n_1
        print(rap_n)
    er_n_1 = er_n
    
print()

'''
         (b-a)/2                   (b-a)/2
     /---------------------\ /----------------------\/
    |   (b-a)/4    (b-a)/4  |                        |
  b |-----------|-----------|------------|-----------|b
        x2 = (a + x1)/2         x1 = (a+b)/2
        
     f(a) * f(x) < 0 => radacina E [a,x]
     f(b) * f(x) < 0 => radacina E [x,b]   
'''

import numpy as np
from scipy.optimize import fsolve

def my_bisection(f, a, b, tol): 
    # approximates a root, R, of f bounded 
    # by a and b to within tolerance 
    # | f(m) | < tol with m the midpoint 
    # between a and b Recursive implementation
    
    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs(f(m)) < tol:
        # stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return my_bisection(f, a, m, tol)

f = lambda x: x**2 - 2

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)

print("f(r1) =", f(r1))
print("f(r01) =", f(r01))    
 
my_bisection(f, -2, -1, 0.001)
r1_exact = fsolve(f,-2)   
er_abs = abs(r1_exact - r1) 
print()
print(er_abs)

def bisectie_iter(f, a, b, n):
    for i in range(n):
        x = (a+b)/2
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0 :
            b = x
        elif f(b) * f(x) < 0 :
            a = x
        else: 
           raise Exception('Nu se poate aplica met.bis!')
    return x         

print()
print("Iter: ")
print()
r1_exact = fsolve(f, -2)

er_abs = abs(r1_exact - r1)
r1_iter = bisectie_iter(f, -2, -1 ,10)

print("r1_exact: " , r1_exact)
print("er_abs: ", er_abs)
print("r1_iter: ", r1_iter)

def bisectie_tol(f, a, b, tol):
    er = tol+1
    i=0
    while er > tol:
        x = (a+b)/2
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0 :
            b = x
        elif f(b) * f(x) < 0 :
            a = x
        else: 
           raise Exception('Nu se poate aplica met.bis!')
    er = abs(r1_exact - x)
    i += 1   
    return x    

print()
print("Tol:")
print()
r1_exact = fsolve(f, -2)

er_abs = abs(r1_exact - r1)
r1_iter = bisectie_tol(f, -3, -1 ,10)     

print("r1_exact: " , r1_exact)
print("er_abs: ", er_abs)
print("r1_iter: ", r1_iter)

r1_tol, nr_iter = bisectie_tol(f, -2, -1, 10**-5)

print()

print("r1_tol: ", r1_tol , " | nr_iter: ", r1_iter)