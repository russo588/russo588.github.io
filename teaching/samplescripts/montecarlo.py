
import random
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return math.exp(x)

n = 100 #number of samples	

x = np.linspace(0,1,50)

Domain = [i for i in x]
Range = [f(i) for i in x]
Sample = [random.random() for i in range(n)] 
FSample = [f(i) for i in Sample]


Average = sum(FSample) / n
print(Average)

scatter = plt.scatter(Sample, FSample, color='red') 

plt.plot(Domain, Range)	
plt.show()