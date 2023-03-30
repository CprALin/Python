import math

#ex 1

#rotunjire in sus
x = 3.25
y = 3.75
z = -3.25
w = -3.75

print("Rotunjire in sus:")
print(math.ceil(x))            
print(math.ceil(y))
print(math.ceil(z))
print(math.ceil(w))            

#rotunjire in jos
print("Rorunjire in jos:")
print(math.floor(x))
print(math.floor(y))
print(math.floor(z))
print(math.floor(w))

#trunchiere
print("Trunchiere:")
print(math.trunc(x))
print(math.trunc(y))
print(math.trunc(z))
print(math.trunc(w)) 

#ex 2
print()
print("ex 2:")

x = 2

print(math.pow(10,x)) 
print(math.pow(x,10))
print(math.pow(x,10.01))
print(math.sqrt(math.pow(10,x)))
print(math.pow(math.sqrt(math.pow(10,x)),5))
print(math.pow(math.e,math.sin(x)))
print(math.pow(math.e,1-math.log(1+math.pow(x,3),x)))
print(math.pow(2,1-math.log(1+math.pow(x,3),x)))
   

