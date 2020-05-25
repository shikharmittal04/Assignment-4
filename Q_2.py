import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer()
n=10000
x=np.zeros(n)

for i in range(n):
	x[i]=np.random.rand()	

end = timer()

print("Time required=",end-start)
plt.hist(x,density=True)
plt.show()
