#function to numerically compute solutions to 2nd order ODE using Eulers method. 

#second order equations can be writen as a system of first order equations. 

def Euler(f, t, y_0, y_1,stepsize, howlong):
	#stepsize	
	h=stepsize

	#end and start
	End=howlong 
	Start=t

	#number of iterations
	n=(End-Start)/h

	#initialize data, basically starting a list of values 
	y=[y_0] 
	y_prime=[y_1]
	time=[t]

	#n will be a float, needs to be turned back into an int. 
	# the following computes using the ith member of the list, appends the i+1 member. 
	for i in range(int(n)): 
		y_prime.append(round(y_prime[i]+h*f(time[i], y[i], y_prime[i]),5))  #rounding to the 5th decimal spot
		time.append(time[i]+h)
		y.append(round(y[i]+h*y_prime[i], 5))	
	return y
	#returns a list of values. 

#some caution: floats do not have infinite precision, if you let this run too long the float will go boom. 