#this script computes the solution for a differential equation using
#4th order Runge Kutta.

import math 
import matplotlib as mpl
import matplotlib.pyplot as plt



#intial conditions
t0=0
y0=1

#defining the function
def f(t,y):
	return -2*y*t

#stepsize	
h=0.01

#end and start
End=2
Start=t0

#storing data
ystar=[y0]
tstar=[t0]

#number of iterations
n=(End-Start)/h

#loop
for i in range(int(n)):
	k_1=h*f(tstar[i],ystar[i])

	k_2=h*f(tstar[i]+h/2,ystar[i]+k_1/2)

	k_3=h*f(tstar[i]+h/2,ystar[i]+k_2/2)

	k_4=h*f(tstar[i]+h,ystar[i]+k_3)

	ystar.append(ystar[i]+(k_1+2*k_2+2*k_3+k_4)/6)
	tstar.append(tstar[i]+h)
#print(ystar)  #remove the comment if you want to see the values its spitting out. 

#plot the solution

plt.plot(tstar, ystar)
plt.show()