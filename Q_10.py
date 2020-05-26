#Question 10
import numpy as np
import scipy.optimize as scop
import matplotlib.pyplot as plt
import emcee
import corner

f=open("Data.txt","r")           	#Read the data given.
Data=f.readlines()
i=0
x=np.zeros(20) 
y=np.zeros(20)
y_er=np.zeros(20)
for D in Data:
    D1,D2,D3,D4=D.split()
    x[i]=float(D2)
    y[i]=float(D3)
    y_er[i]=float(D4)
    i=i+1


def LLH(P, x, y, y_er):
	a, b, c = P
	Mdl = a*x**2+b*x+c
	lnL = -0.5*np.sum((y - Mdl)**2/y_er**2 + np.log(2*np.pi*y_er**2))	#Natural logarithm of likelihood.
	return lnL
	
def prior(P):
	a, b, c = P
	if 0< a <100 and -500 < b < 500 and -500 < c < 500:
		return 1
	else:
		return 0
		
def post(P, x, y, y_er):
	return	LLH(P, x, y, y_er)+np.log(prior(P))
	
P0=(1,1,1)
Sol=scop.minimize(post,P0,args=(x,y,y_er))

MC=50
NOP=3
init = Sol.x + 1e-4 * np.random.randn(MC,NOP)

sampler = emcee.EnsembleSampler(MC,NOP,post,args=(x, y, y_er))
sampler.run_mcmc(init, 4000)

samples = sampler.get_chain()

fig,axs= plt.subplots(3,1,sharex=True)

axs[0].plot(samples[:, :, 0]) # a values
axs[1].plot(samples[:, :, 1]) # b values
axs[2].plot(samples[:, :, 2]) # c values

axs[0].set_ylabel('$a$',fontsize=12)    
axs[1].set_ylabel('$b$',fontsize=12)
axs[2].set_ylabel('$c$',fontsize=12)

for ax in axs.flat:
    ax.label_outer()

M = np.median(samples, axis=0)
A,B,C=np.mean(M,axis=0)

odr = x.argsort()[::1]
x = x[odr]
y=y[odr]

fx=A*x**2+B*x+C

fig1,ax1=plt.subplots()
ax1.plot(x,fx,'r-')
ax1.errorbar(x,y,yerr=y_er,fmt='o',color='b')
print('a,b,c = ',A,' ',B,' ',C)
#fig1 = corner.corner(samples,truths=[A,B,C])
plt.show()
