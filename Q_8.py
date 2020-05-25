#Question 8
import numpy as np
import scipy.special as scsp

n=int(input("Dimensions: "))
N=10000

x=np.zeros((n,N))
for i in range(n):
	x[i][:]=2*np.random.rand(N)-1	# N Random points in an n-D bounding box

k=0
for j in range(N):
	if sum((x[:,j])**2)<=1:			#No.of many which lie inside the volume required 
		k=k+1
		
V=k*2**n/N							# 2^n is the volume of bounding box
Vn=np.pi**(n/2)/scsp.gamma(1+n/2)	#Actual volume of n-D sphere.
E=Vn-V
print('Monte Carlo volume estimate:',V)
print('Analytical result:',Vn)
print('Absolute Error',E)
