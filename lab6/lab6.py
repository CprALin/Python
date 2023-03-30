import numpy as np
from numpy.polynomial import Polynomial as P
from math import factorial,exp
from time import perf_counter

#Exercitiul 4 

#val exacta va fi calculata cu Polynomial

x = 4.71

# (a) - sintaxa python

f = x**3 - 6.1*x**2 + 3.2*x + 1.5

print(f)

print()
#(b) 

a = [1, -6.1, 3.2, 1.5]
a = np.array(a)

f_horner = a[0]

for c in range(1,len(a)):
    f_horner = f_horner*x + a[c]

print(f_horner)
print()


#(c) - valoarea exacta
p = P(a[::-1])
f_exact = p(x)

print(f_exact)
print()

#eroarea aboluta & relativa pentru (a)

er_abs_a = abs(f_exact-f)
er_rel_a = er_abs_a/abs(f_exact)
print(er_abs_a , " | ", er_rel_a)
print()

#erroarea absoluta & relativa pentru (b)

er_abs_b = abs(f_exact-f_horner)
er_rel_b = abs(f_exact-f_horner)
print(er_abs_b," | ",er_rel_b)
print()

'''
#schema lui Horner generalizata

#   a3         a2         a1    a0
f = 1*x**3 - 6.1*x**2 + 3.2*x + 1
#   b2        b1   b0
g = a*x**2 + 1*x + 1

#rest

r_x = 9.3*x + 8.6

#cat
c_x = x - 7.1

f = c_x*g + r_x

'''

#Exercitiul 5 

def myexp(x,n):
    e = 0
    for i in range(n):
        e += (x**i)/factorial(i)
    return e    

x = 1
n = 5

#(a)
exp_aprox_5 = myexp(x,n)
print(exp_aprox_5)
print()

#(b)

n = 10

t0 = perf_counter()

exp_aprox_10 = myexp(x,n)

t1 = perf_counter()

print(t1-t0)

print(exp_aprox_10)
print()

exp_exact = exp(1)
er_abs_5 = abs(exp_exact-exp_aprox_5)
er_rel_5 = er_abs_5/abs(exp_exact)

er_abs_10 = abs(exp_exact-exp_aprox_10)
er_rel_10 = er_abs_10/abs(exp_exact)

print(er_abs_5 ,' | ', er_rel_5)
print()
print(er_abs_10 ,' | ', er_rel_10)
print()

def myexp2(x,n):
    e = 0
    ei = 1
    for i in range(1,n):
        e += ei
        ei = ei*x/i
    return e 

t0 = perf_counter()

exp_aprox_10 = myexp2(x,n)

t1 = perf_counter()

print()
print(t1-t0)
print()
#Exercitiul 6

i = 0
e = 0
ei = 1
e += ei
er_abs = abs(exp_exact - e)
er_rel = er_abs/abs(exp_exact)

while(er_rel > 10**(-14)):
    i += 1

print(i)
print()   