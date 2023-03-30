import numpy as np
from matplotlib import pyplot as plt

x = np.arange(5,20.5,.5)

y1 = 10**x
y2 = x**10
y3 = x**10.01
y4 = np.sqrt(10**x)
y5 = np.sqrt(10**x)**5
y6 = np.e**np.sin(x)
y7 = np.e**1-np.log(1+x**3,x)
y8 = 2**np.log(1+x**3,x)

plt.subplot(2,4,1)
plt.plot(x,y1)
plt.subplot(2,4,2)
plt.plot(x,y2)
plt.subplot(2,4,3)
plt.plot(x,y3)
plt.subplot(2,4,4)
plt.plot(x,y4)
plt.subplot(2,4,5)
plt.plot(x,y5)
plt.subplot(2,4,6)
plt.plot(x,y6)
plt.subplot(2,4,7)
plt.plot(x,y7)
plt.subplot(2,4,8)
plt.plot(x,y8)

fig = plt.figure()
plt.plot(x,y7)
plt.scatter(x,y8)
plt.title(r'$\phi_7\ and \ \phi_8$')
plt.xlabel('Var. idependenta')
plt.ylabel('Var. dependenta')
plt.legend(['functia g','functia h'])
plt.axis([0,30,0,.5])
plt.ylim(0,.5)
plt.xticks(np.arange(0,30,10),['zero','10','20'])



plt.show()