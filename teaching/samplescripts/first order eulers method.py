import math
import matplotlib.pyplot as plt

def f(x,y):
	return -.5 * math.exp(x/2) * math.sin(5*x) + 5 * math.exp(x/2) * math.cos(5*x) + y

def solution(x):
	return math.exp(x/2) * math.sin(5*x)

[start_x, start_y] = [0,0]

h = .05
x = [start_x]
y = [start_y]

for i in range(100):
	x.append(x[i] + h)
	y.append(y[i] + h * f(x[i], y[i]))

true = [solution(x) for x in x]

plt.plot(x, y, 'b')
plt.plot(x, true, 'k.')

plt.show()


