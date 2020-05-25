#Question 9
import numpy as np
import matplotlib.pyplot as plt

def f(z):
	if 3<z<7:
		return 1		#The normalisation of required PDF is not required (though the correct value is 1/4).
	else:
		return 0

N=int(input('Morkov chain length = '))
x=np.zeros(N)
x[0]=5					#I chose this starting point in order to avoid division by 0.
						#In a certain run, you may get an error, in such a situation 
						# try re-running the code.
for k in range(N-1):
	x_1=np.random.normal(x[k], 1)
	r=np.random.rand()
	if f(x_1)/f(x[k])>r:
		x[k+1]=x_1
	else:
		x[k+1]=x[k]

plt.subplot(1,2,1)
plt.plot(x)
plt.xlabel('Index')
plt.ylabel('x')
plt.title('Markov chain')

plt.subplot(1,2,2)
plt.hist(x,bins=100,density=True)

X=np.linspace(3,7,100)
Y=1/4*np.ones(100)		#Just for comparision, plot the analytical PDF we know with correct normalisation.
plt.plot(X,Y,'r-')
plt.title('PDF')
plt.show()
