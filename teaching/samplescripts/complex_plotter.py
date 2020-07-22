
import cmath
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
r=2 #make a 2r x 2r square around 0. 
X = np.arange(-r, r, 0.01)
Y = np.arange(-r, r, 0.01)
X, Y = np.meshgrid(X, Y)

def z(x,y):
    return x + 1j * y
z = z(X, Y) #makes an grid of complex numbers

def zbar(x,y):
    return x - 1j * y
zbar = zbar(X, Y)

Im = Y #renaming for clarity
Re = X #ditto


#everything is computed on a grid of numbers. 
# f= z*z-1 #an example with polys that doesnt need cmath
f=np.vectorize(cmath.sqrt)(z) #cmath does not get along with arrays, this fixes that. 
imf=f.imag
ref=f.real
Mod=np.sqrt(f.imag**2+f.real**2)


#color mapping
norm=mpl.colors.Normalize(-np.pi,np.pi)
my_col = cm.hsv(norm(np.arctan2(f.imag,f.real))) #hsv is a cyclic color map
floor_col = cm.hsv(norm(np.arctan2(Im,Re)))



surf = ax.plot_surface(X, Y, Mod, facecolors = my_col, linewidth=0, antialiased=False) #surface color
bottom = ax.plot_surface(X, Y, 0*X, facecolors = floor_col, linewidth=0, antialiased=False) #floor color for ref


# Customize the z axis.
maxvalue=np.amax(Mod)
ax.set_zlim(0, maxvalue)


plt.show()

