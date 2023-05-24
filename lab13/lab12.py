import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
'''metadata = dict(title='Bernstein01', artist='Matplotlib', comment='Bernstain Approximation Polynomial)
writer = writers['ffmpeg']
writer = writer(fps=1, metadata=metadata)
fig = plt.figure()'''

n = 4
a = np.random.randint(1, 10, (n, n))
b = np.random.randint(1, 10, (n, 1))
a = a.astype(float)

L = np.eye(n)
L = L.astype(float)

def eliminareGauss():
    aux = a.copy()
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            L[i, j] = aux[i][j] / aux[j][j]
            aux[i][j] = 0
            aux[i][j + 1:] -= (L[i][j] * aux[j][j + 1:])
    return aux

U = eliminareGauss()
A = L@U

print("A:\n", a)
print("L:\n", L)
print("U:\n", U)
print("L * U:\n", L @ U)
print("Este L * U egal cu A?", np.allclose(L @ U, a))
'''
x = np.zeros(n)
def substitutieInapoi():
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        s = np.dot(a[i, i + :1], x[i + 1:])
        x[i] = (1/a[i, i]) * (b[i] - s)
    return x

x= substitutieInapoi()

print(a, b, x_ex, ae, x)'''

x = np.zeros(n)

def substitutieInainte():
    x[0] = b[0] / L[0, 0]
    for i in range(1, n):
        s = np.dot(L[i, :i], x[:i])
        x[i] = (1 / L[i, i]) * (b[i] - s)
    return x

x_sust_inainte = substitutieInainte()

print("Solutia cu substitutie inainte:\n", x_sust_inainte)
'''
a = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
L = np.eye(n)
U = a.copy()

for j in range(2, n): 
    U[1, j] = a[1, j]/L[1, 1]
    L[0, j] = a[j, 0]/U[0, 0]
    
def LU():
    for i in range(1, n - 1):
        s = np.dot(L[i, :i], U[:i, i])
        if a[i, i] - s != U[i, i]:
         return
    for j in range(i, n):
        U[i, j] = (1/L[i, i]) * (a[i, j] - np.dot(L[i, :i]))
        L[j, i] = (1/U[i, i]) * (a[j][i] - np.dot(L[j, i]))
    s = np.dot(L[n - 1, :n - 1], U[:n - 1, n - 1])
    if L[n - 1, n - 1] * U[n - 1, n - 1] : a[n - 1, n - 1] - s
'''    