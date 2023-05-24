import numpy as np

n = 4
a = np.random.randint(1, 10, (n, n))
b = np.random.randint(1, 10, (n, 1))

x_ex = np.linalg.solve(a,b)

#Eliminare Gauss
ae = np.hstack((a, b))
ae = ae.astype(float)
for j in range (n-1):
    for i in range (j+1, n):
        m = ae[i, j]/ae[j, j]
        ae[i, j] = 0
        ae[i, j+1:] -= m * ae[j, j+1:]


b = ae[:, -1]
a = ae[:, :n]

print (b)
print(" ")
print (a)

#Substitutia inapoi
x = np.zeros(n)
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range (n-2,-1, -11):
    sum = 0
    sum = np.dot(a[i, i+1:], x[i+1])
    x[i] = (1 / a[i, i]) * (b[i] - sum)

print("Substitutie inapoi")
print(x)
print(x_ex)