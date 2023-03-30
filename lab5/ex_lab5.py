import math

#ex 1

print("_Ex_1_:")
print()

x = 5/7
y = 1/3
u = 0.714251
fl_x = 0.71428
fl_y = 0.33333

s = x + y
fl_s = fl_x + fl_y
er_abs = abs(s-fl_s)
er_rel = er_abs/abs(s)

print("_Suma_: ")
print()
print("Suma: " , s)
print("Suma_fl: " , fl_s)
print("Err_Abs: " , er_abs)
print("Err_Rel: " , er_rel)
print()

d = x - y
fl_d = fl_x - fl_y
er_abs2 = abs(d-fl_d)
er_rel2 = er_abs2/abs(d)

print("_Diferenta_:")
print()
print("Diferenta: ", d)
print("Dif_fl: ", fl_d)
print("Err_Abs: ", er_abs2)
print("Err_Rel: ", er_rel2)
print()

p = x * y
fl_p = fl_x * fl_y
er_abs3 = abs(p-fl_p)
er_rel3 = er_abs3/abs(p)

print("_Produs_:")
print()
print("Produs: ", p)
print("Prod_fl: ", fl_p)
print("Er_Abs: ", er_abs3)
print("Er_Rel: ", er_abs3)
print()

c = x / y
fl_c = fl_x / fl_y
er_abs4 = abs(c-fl_c)
er_rel4 = er_abs4/abs(c)

print("_Cat_:")
print()
print("Cat: ", c)
print("Cat_fl: ", fl_c)
print("Er_Abs: ", er_abs4)
print("Er_Rel: ", er_rel4)
print()

#ex 2 

print("_Ex_2_:")
print()

x = 5/7
u = 0.714251
v = 98765.9
w = 0.1111111 * 10 ** -4
fl_x = 0.71428
fl_u = 0.71425 * 10 ** 0
fl_v = 0.98765 * 10 ** 5
fl_w = 0.111111 * 10 ** -4

val_exacta1 = x - u
val_aprox1 = fl_x - fl_u
er_abs1 = abs(val_exacta1-val_aprox1)
er_rel1 = er_abs1/abs(val_exacta1) 


print("OP1:")
print()
print("Val exacta: ", val_exacta1)
print("Val aprox: ", val_aprox1)
print("Er_Abs: ", er_abs1)
print("Er_Rel: ", er_rel1)
print()

val_exacta2 = (x-u)/w
val_aprox2 = (fl_x - fl_u) / fl_w
er_abs2 = abs(val_exacta2-val_aprox2)
er_rel2 = er_abs2/abs(val_exacta2)

print("OP2:")
print()
print("Val exacta: ", val_exacta2)
print("Val aprox: ", val_aprox2)
print("Er_Abs: ", er_abs2)
print("Er_Rel: ", er_rel2)
print()

val_exacta3 = (x-u)*v
val_aprox3 = (fl_x - fl_u) * fl_v
er_abs3 = abs(val_exacta3 - val_aprox3)
er_rel3 = er_abs3 / abs(val_exacta3)

print("OP3:")
print()
print("Val exacta: ", val_exacta3)
print("Val aprox: ", val_aprox3)
print("Er_Abs: ", er_abs3)
print("Er_Rel: ", er_rel3)
print()

val_exacta4 = u + v
val_aprox4 = fl_u + fl_v
er_abs4 = abs(val_exacta4 -val_aprox4)
er_rel4 = er_abs4 / abs(val_exacta4)

print("OP4:")
print()
print("Val exacta: ", val_exacta4)
print("Val aprox: ", val_aprox4)
print("Er_Abs: ", er_abs4)
print("Er_Rel: ", er_rel4)
print()

#Ex 3

a = 1 
b = 62.10
c = 1

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta))/2*a
x2 = (-b - math.sqrt(delta))/2*a

fl_x1 = -0.01610723
fl_x2 = -62.08390

er_abs_1 = abs(x1 - fl_x1)
er_rel_1 = er_abs_1 / abs(x1)

er_abs_2 = abs(x2 - fl_x2)
er_rel_2 = er_abs_2 / abs(x2)

print("_Ex3_:")
print()
print("x1 = ", x1, " x2 = ",x2)
print("Er_abs_x1: ", er_abs_1)
print("Er_Rel_x1: ", er_rel_1)
print("Er_abs_x2: ", er_abs_2)
print("Er_rel_x2: ", er_rel_2)