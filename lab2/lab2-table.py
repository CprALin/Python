import numpy as np

l = [1,2,3,4,5,6,7,8,9,10] #lista
a = np.array(1) #tablou 1D

#ex 1
a = np.random.rand(4,3) * 2 + 8 # *(b-a) + a -> [a,b) | (b-a) - scalare | +a - translatie 

a = np.random.rand(4,3) * (-2) + 10

print(a)
#ex 2
a1 = np.random.randint(5,11,(3,10))

#ex 3
a1[:2,-3:]

print(a1)
#ex 4
a2 = np.zeros(30) + 2

#ex 5
a2 = np.reshape(a2, (3,10))
print(a2)

#ex 6 
p = a2**a1 #a2[i,j]**a1[i,j]
print(p)

#ex 7
p2 = a1**2
print(p2)

#ex 8
a1[:,0] #prima coloana din matricea a1

n= np.linalg.norm(a1[:,0]) #norma implicita = norma 2 = norma euclidiana

