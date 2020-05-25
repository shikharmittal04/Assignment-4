#Shikhar Mittal, DTP
#Assignment-4
#Question 1
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer()
m=2**31
a=1103515245
c=12345
n = 10000
x = np.zeros(n)
x[0]=1

for i in range(n-1):
	x[i+1] = (a*x[i]+c)%m

x=x/m	#To scale the data between 0 to 1.
end=timer()
print("Time required=",end-start)
plt.hist(x,density=True)
plt.show()
