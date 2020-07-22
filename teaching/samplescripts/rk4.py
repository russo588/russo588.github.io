#RK4 
#will return a list of iterates

#this will work on numpy arrays (which are like vectors). See the vect-field example. 

#Solves first order equations of the form dy/dt=F(y,t). 
#t0 and y0 are the initial conditions. 

def RK4vect(F, t_0, y_0, timeinterval, stepsize):
	from math import floor
	h=stepsize
	T=timeinterval
	n=floor(T/h)
	ystar=[y_0]
	tstar=[t_0]
	#loop
	for i in range(int(n)):
		k_1=h*F(tstar[i],ystar[i])

		k_2=h*F(tstar[i]+h/2,ystar[i]+k_1/2)

		k_3=h*F(tstar[i]+h/2,ystar[i]+k_2/2)

		k_4=h*F(tstar[i]+h,ystar[i]+k_3)

		ystar.append(ystar[i]+(k_1+2*k_2+2*k_3+k_4)/6)
		tstar.append(tstar[i]+h)
	return ystar







