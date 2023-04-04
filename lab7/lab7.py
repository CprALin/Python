from math import modf, sqrt, exp, log, log2, sin

#ex 5
def myexp(x, n):
    ei = 1
    e = 0
    e += ei
    for i in range(1, n):
        #e +=  (x**i)/factorial(i)
        ei *= (x/i)
        e += ei
    return e


#ex7

print("Ex 7:")

p = 1 
pf,pi = modf(sqrt(5))
pi = int(pi)

for i in range(pi):
    p *= myexp(1,100)

p *= myexp(pf,100)

e_sqrt5 = exp(sqrt(5))

er_abs_e_sqrt5 = abs(e_sqrt5 - p)
er_rel_e_sqrt5 = er_abs_e_sqrt5/abs(e_sqrt5)

print("Err_Abs: ", er_abs_e_sqrt5, " | Err_Rel:" , er_rel_e_sqrt5)
      
print()
      
#ex8

print("Ex8:")

def myln(z, n):
    x = (1 - z)/(1 + z)
    ln = 0
    for i in range(n):
        ln += (x ** (2 * i + 1))/(2 * i + 1)
    ln = (-2) * ln
    return ln
     
ln7_aprox = myln(7,10)
ln7_exact = log(7)
er_abs_ln7 = abs(ln7_exact-ln7_aprox)
er_rel_ln7 = er_abs_ln7/abs(ln7_exact)

print("Err_Abs: ", er_abs_ln7, " | Err_Rel:" , er_rel_ln7)    

print()
print("Ex_myln_er:")
def myln_er(z, er):
    x = (1 - z)/(1 + z)
    ln = 0
    er_rel = er + 1
    i = 0
    while(er_rel > er):
        ln += (-2) * (x ** (2 * i + 1))/(2 * i + 1)
        er_rel = abs(ln - log(z))/abs(log(z))
        i += 1
    return ln

ln7_aprox_er = myln_er(7, 10**(-14))
ln7_exact_er = log(7)
er_abs_ln7_er = abs(ln7_exact_er-ln7_aprox_er)
er_rel_ln7_er = er_abs_ln7_er/abs(ln7_exact_er)

print("Err_Abs: ",er_abs_ln7_er , " | Err_Rel:" , er_rel_ln7_er )  

print()

#log2(3) ?

print("Ex_log2:")

log23_exact = log2(3)
log23_aprox = myln(3, 10)/myln(2, 10)

er_abs_log23 = abs(log23_exact-log23_aprox)
er_rel_log23 = er_abs_log23/abs(log23_exact)

print("Err_Abs: ", er_abs_log23, " | Err_Rel:" ,er_rel_log23)  
print()

print("Ex_mysin:")

def mysin(x,n):
    ui = x
    s = ui
    for i in range(1,n):
        ui *= (-1)*(x**2)/(2*i*(2*i+1))
        s += ui
    return s

sin23_aprox = mysin(23,10)
sin23_exact = sin(23)    

er_abs = abs(sin23_aprox-sin23_exact)
er_rel = er_abs/abs(sin23_exact)

print("Err_Abs: ", er_abs, " | Err_Rel:" ,er_rel)  
print()
#Ex9 

print("Ex_9:")

def mysqrt(alpha,n):
    alpha = 89
    x = alpha
    for i in range(n):
        x = (x+alpha/x)/2
    return x
    
sqrt89_aprox = mysqrt(89,10)
sqrt89_exact = sqrt(89)
er_abs = abs(sqrt89_aprox-sqrt89_exact)
er_rel = er_abs/abs(sqrt89_exact)

print("Err_Abs: ", er_abs, " | Err_Rel:" ,er_rel)  