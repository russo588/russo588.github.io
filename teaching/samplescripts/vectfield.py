import numpy as np 
import matplotlib.pyplot as plt
from rk4 import RK4vect #importing my RK4 function 
import matplotlib.cm as cm # this is for color maps

#I am defining what color map I want to use. Color maps take in a value from (0,1) return a color. 
colormap=cm.jet

#picking a range of x and y Values. 
x = np.arange(-2,2.1,0.1)
y = np.arange(-2,2.1,0.1)

#this makes an grid of numbers from the ranges above. 
X, Y = np.meshgrid(x, y)
# print(X,Y) remove the comment if you want I mean. 

#This is defining the vector field for the plot. The quiver function will call this. 
U, V = Y-X,  -X-Y

#starts the figure, needs to be up here since I plot the trajectories in the loop below. 
figure, ax=plt.subplots()

#I am defining the function to run RK4 on.
# RK4vect returns a list of values to trajectories to differential equations of the form: dy/dt=F(t,y). 
#Here y can be a vector and t is a scalar time component. 

def F(t,x):
	return np.array([x[1]-x[0], -x[0]-x[1]]) 
#this function has no dependence of time. Its solely a function from R2 to R2. 
# the inputs x are numpy arrays. x=[x[0],x[1]]. 	

#This will produce two sets of trajectories, starting at (-2,0) and (2,0) and iterating upward. 
for number in [-2,2]:
	for i in range(0,11):
		y=np.array([number,-2+.4*i]) #This is defining the start of the trajectory.
		result=RK4vect(F,0,y,5,0.1) #running RK4 with the set initial condtions, I picked t=0 arbitrarily. 
		xcoor=[] #starting a list of x coordinates. 
		ycoor=[] #starting a list of y coordinates.

		# the result of RK4vect will be a list of arrays, I am peeling off the first and second coordinates. 
		for j in range(len(result)):
			xcoor.append((result[j])[0])
			ycoor.append((result[j])[1])

		plt.plot(xcoor,ycoor, color=colormap(.1*i)) #plotting the trajectories, color defined by the color map. 



ax.quiver(X, Y, U, V, color='k', width=.0009) #this plots the vector field 
plt.show() #show off your work. 