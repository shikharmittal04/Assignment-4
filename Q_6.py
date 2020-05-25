import numpy as np
import matplotlib.pyplot as plt

def erf(x):
	return np.sqrt(2/np.pi)*np.exp(-x**2/2)

N=1000
x=5*np.random.rand(N)
fx=0.8*np.random.rand(N)
#x=np.sqrt(2)*np.tan(x/np.sqrt(2))


#fx=np.random.rand(N)*1/(1+0.5*x**2)
Y=fx[fx<erf(x)]
X=x[fx<erf(x)]

Q=np.linspace(0,5,100)
W=erf(Q)

plt.subplot(1,2,1)
plt.scatter(x,fx,color='b')
plt.scatter(X,Y,color='g')
plt.plot(Q,W,'r')
plt.plot(Q,0.8*np.ones(100),'k')

plt.subplot(1,2,2)
plt.hist(X,range=(0,5),bins=100,density='True')
plt.plot(Q,W,'r-')
plt.show()
