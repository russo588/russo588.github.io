
import math
from PIL import Image
CD={'red':(252,3,3), 'orangered': (252,73,3), 'orange': (252,140,3), 'orangeyellow': (252,198,3), 'yellow': (252,236,3), 'yellowgreen':(219,252,3), 
    'greenyellow':(152,252,3), 'green':(57, 252, 3), 'greenblue': (3,252,107), 'teal': (3,252,198), 'cyan':(3,219,252), 'periwinkle':(3,148,252), 
    'lightblue':(3,78,252), 'blue': (19,3,252), 'darkblue':(10,0,156), 'navy':(6,1,82), 'reallydarkblue':(1,1,50), 'black':(0,0,0)}
w, h, zoom = 1200, 1000, 1
   
# creating the new image in RGB mode 
fractal = Image.new("RGB", (w, h)) 
  
# loading the pixel data. 
pixel = fractal.load() 
     
# setting up the variables according to  
# the equation to  create the fractal 
cX, cY = -.7269, .1889
moveX, moveY = 0.0, 0.0 #moves the center
maxIter = 512
bin = 32 
#coloring based on 'escape time' and with some handpicked color
for x in range(w): 
    for y in range(h): 
        zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX 
        zy = 1.5 * (y - h / 2) / (0.5 * zoom * h) + moveY 
        i = maxIter 
        while zx*zx + zy*zy < 4 and i > 1: 
            tmp = zx*zx - zy*zy + cX 
            zy,zx = 2.0*zx*zy + cY, tmp 
            i = i-1
        if i==maxIter:
            pixel[x,y]=CD['reallydarkblue']
        elif i>15*bin and i<16*bin:
            pixel[x,y]=CD['navy']
        elif i>14*bin and i<=15*bin:
            pixel[x,y]=CD['darkblue']
        elif i>13*bin and i<=14*bin:
            pixel[x,y]=CD['blue']
        elif i>12*bin and i<=13*bin:
            pixel[x,y]=CD['lightblue']
        elif i>11*bin and i<=12*bin:
            pixel[x,y]=CD['periwinkle']
        elif i>10*bin and i<=11*bin:
            pixel[x,y]=CD['cyan']
        elif i>9*bin and i<=10*bin:
            pixel[x,y]=CD['teal']
        elif i>8*bin and i<=9*bin:
            pixel[x,y]=CD['greenblue']
        elif i>7*bin and i<=8*bin:
            pixel[x,y]=CD['green']
        elif i>6*bin and i<=7*bin:
            pixel[x,y]=CD['greenyellow']
        elif i>5*bin and i<=6*bin:
            pixel[x,y]=CD['yellowgreen']
        elif i>4*bin and i<=5*bin:
            pixel[x,y]=CD['yellow']
        elif i>3*bin and i<=4*bin:
            pixel[x,y]=CD['orangeyellow']
        elif i>2*bin and i<=3*bin:
            pixel[x,y]=CD['orange']
        elif i>1*bin and i<=2*bin:
            pixel[x,y]=CD['orangered']
        else:
            pixel[x,y]=CD['black']
            
# to display the created fractal 
fractal.show()
#fractal.save("Julia_set.png")