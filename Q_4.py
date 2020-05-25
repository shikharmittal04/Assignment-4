# WARNING!: Run this code only after you have run "Q_4.c"
# To plot the results of C code.
import numpy as np
import matplotlib.pyplot as plt
f=open("Q_4.txt","r")           	#Read the data obtained from C.
Data=f.readlines()
i=0
N=10000                            	#This N should be the same as used in the corresponding C code.
x=np.zeros(N) 
y=np.zeros(N)
for D in Data:
    D1,D2=D.split()
    x[i]=float(D1)
    y[i]=float(D2)
    i=i+1

X=np.linspace(0,10,1000)           	
Y=2*np.exp(-2*X)                	#Exponential PDF.

plt.subplot(1,2,1)
plt.hist(x,density='True')
plt.title('Uniform PDF',fontsize=14)

plt.subplot(1,2,2)
plt.hist(y,bins=100,density='True')    		#From the C code.
plt.plot(X,Y,'r')                   #Analytical result.
plt.legend(['From C using rand()','Analytical'],fontsize=14)
plt.title('Exponential PDF',fontsize=14)

plt.grid(True)
plt.show()
