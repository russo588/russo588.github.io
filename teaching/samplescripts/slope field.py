import math
from numpy import linspace
from numpy import seterr
import matplotlib.pyplot as plt

# dy/dx= x^2-y for this demonstration.
def f(x,y):
	return x**2 - y

#defines a function to plot a slopefield. 
def slopefield(g, x_1, x_2, x_density, y_1, y_2, y_density, length):
	seterr(all='ignore') #ignoring the warnings, none are serious. 

	def segment(x,y,d):
		slope_value = f(x,y)
		first_pt = (x + 1, y + slope_value)
		second_pt = (x - 1, y - slope_value)
		distance = math.sqrt((first_pt[0] - second_pt[0])**2 + (first_pt[1] - second_pt[1])**2)
		first_pt = (x + (.5 * d / distance) * (first_pt[0]-x), y + (.5 * d / distance) * (first_pt[1] - y))
		second_pt = (x + (.5 * d / distance) * (second_pt[0]-x), y + (.5 * d / distance) * (second_pt[1] - y))
		return [[first_pt[0], second_pt[0]], [first_pt[1], second_pt[1]]]

	horizontal = linspace(x_1, x_2, x_density)
	vertical = linspace(y_1, y_2, y_density)

	for x in horizontal:
		for y in vertical:
			X = segment(x, y, length)[0]
			Y = segment(x, y, length)[1]
			plt.plot(X, Y, 'b')  #'b' controls the color for the slopefield. 
	plt.show()

#plots a solution for the differential equation in red. 
c = -1
x_coor = [x for x in linspace(-3.15, 3, 100)]
y_coor = [x**2 - 2 * x + 2 + c*math.exp(-x) for x in x_coor]
plt.plot(x_coor, y_coor, 'r')


slopefield(f, -5, 5, 20, -5, 5, 20, .75)
			


print(((-2)**2)**(1/3))
print((-2)**(2/3))


