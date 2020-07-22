#simulates a cannon ball using Eulers method. 

import math #for math stuff
from Euler_2nd_order import Euler #importing my function Euler
import matplotlib as mpl #for plotting
import matplotlib.pyplot as plt #ditto

#picking enough time to hit the floor but not so much float goes boom. Dialed in by hand. 
t1=10.15
t2=14.7

#drag factor
# this is actually a pretty reasonable value assuming the cannon ball is 1 ft-ish in diameter
d=.01


#this is in general how python defines functions. I am going to run two simulation, one with air resistance and one without. 

def gravity(t,y,y_prime):
	return -9.8
def gravity_withair(t,y,y_prime):
	return -9.8 + math.copysign(1,-y_prime)*.5*d*abs(y_prime)**2 #the copysign is the give it direction. 
def cannon_withair(t,y, y_prime):
	return -.5*d*y_prime**2
def cannon(t,y, y_prime):
	return 0
#Euler(force, start time, int pos, int vel, stepsize, timeframe)

# shooting a cannon at 100 m/s  at an angle of 45 deg. 
#Im calling the function to return the list of values. 
y=Euler(gravity_withair, 0, 0, 70.71, 0.01, t1)
x=Euler(cannon_withair, 0, 0, 70.71, 0.01, t1)
y2=Euler(gravity, 0,0,70.71,0.01,t2)
x2=Euler(cannon, 0,0,70.71,0.01,t2)


#plot(list1, list2) plots the values in list1 and list2 as a coordinate pair. 
plt.plot(x,y)
plt.plot(x2,y2)

plt.show()
