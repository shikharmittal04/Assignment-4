#Question 5: Box-Muller method.
import numpy as np
import matplotlib.pyplot as plt

x1=np.random.rand(10000)
x2=np.random.rand(10000)
y1=np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.subplot(1,2,1)
plt.hist(x1,density='True')
plt.title('Uniform PDF',fontsize=14)

plt.subplot(1,2,2)
plt.hist(y1,bins=100,density='True')

X=np.linspace(-5,5,100)
Y=np.sqrt(1/2/np.pi)*np.exp(-X**2/2)		
plt.plot(X,Y,'r')                   		#Analytical result.
plt.title('Gaussian PDF',fontsize=14)

plt.grid(True)
plt.show()
