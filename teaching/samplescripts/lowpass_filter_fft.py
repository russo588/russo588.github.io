
import numpy as np
from math import floor 
from math import exp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#lets us deal with the opacity/alpha channel separately. 
def opacity(rgb):
    return rgb[:, :, 3]

#this function will scoop up the process of transforming, centering, applying the filter, then untransforming.
def Filter(channel, s1, s2):
	ft = np.fft.fft2(channel)
	cft = np.fft.fftshift(ft) 

	cx, cy = floor(cft.shape[0]/2), floor(cft.shape[1]/2)

	sigx, sigy = s1, s2 

	Gauss = np.ones((cft.shape[0], cft.shape[1]))
	for i in range(len(Gauss)):
	        for j in range(len(Gauss[i])):
	        	Gauss[i,j] = exp(-(((i-cx)/sigx)**2 + ((j-cy)/sigy)**2))
	
	filtered = np.fft.ifft2(Gauss*cft)
	
	return filtered

#read in image
img = mpimg.imread('yourimage.png')   

#initializing final result.
result = np.zeros(img.shape)

#handle the alpha channel separately.
opacity_channel = opacity(img)	
opacity_part = np.zeros(img.shape)
opacity_part[:,:,3] = opacity_channel

#We're going to loop over the color channels. We will also use the same values for s1 and s2 for all.  
for i in range(3):
	channel = img[:, :, i]
	filtered = Filter(channel, 20, 20)
	part = np.zeros(img.shape)
	part[:,:,i] = abs(filtered)
	result = result + part

result = result + opacity_part

#display the results. 
plt.figure() 
plt.title('blurred image')
plt.imshow(result)


plt.figure() 
plt.title('original')
plt.imshow(img)

plt.show()









