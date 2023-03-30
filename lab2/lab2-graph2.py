import numpy as np
import matplotlib
from matplotlib import pyplot as plt

m=3
n=4
x=np.arange(20) #vectorul de la 0 la 19

plt.subplot(m,n,1)
plt.plot(x, np.sin(x))
plt.subplot(m,n,11)
plt.plot(x, np.cos(x))
plt.subplot(m,n, 12)
plt.plot(x,np.exp(x))

plt.show()

plt.scatter(x, 2*x, color="green")
plt.show()

f=plt.figure()
plt.scatter(x,2*x,color="red")

plt.figure()
plt.plot(x,np.sin(x),color="black",label="sin")
plt.plot(x,np.cos(x),color="green",label="cos")
plt.legend()
plt.title("titlu")

