import numpy as np
import scipy.stats as scat

n=144	#No.of runs
k=10	#Degrees of freedom
Ps=np.array([1,2,3,4,5,6,5,4,3,2,1])/36
Ys1=np.array([4,10,10,13,20,18,18,11,13,14,13])
Ys2=np.array([3,7,11,15,19,24,21,17,13,9,5])

V=np.zeros(2)
p=np.zeros(2)
V[0]=sum((Ys1-n*Ps)**2/(n*Ps))
V[1]=sum((Ys2-n*Ps)**2/(n*Ps))
p[0]=1-scat.chi2.cdf(V[0], k)
p[1]=1-scat.chi2.cdf(V[1], k)

for i in [0,1]:
	print("v=",V[i],"and P(V>v)=",p[i])
	if p[i]<0.01 or p[i]>0.99:
		print("Not sufficiently random!\n")
	elif 0.01<=p[i]<0.05 or 0.95<p[i]<=0.99:
		print("Suspected!\n")
	elif 0.05<=p[i]<0.1 or 0.9<p[i]<=0.95:
		print("Almost suspected!\n")
	elif 0.1<=p[i]<=0.9:
		print("Sufficiently random!\n")

