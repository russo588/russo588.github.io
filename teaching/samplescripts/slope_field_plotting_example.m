%{This sample script creates a slope field for dy/dx=x^2-y%}
[X,Y]=meshgrid(-5:.2:5,-5:.2:5);%{creates a grid of points from -5 to 5 on the x and y axis with a step size of .2%}
dY=X.^2-Y; %{creates a matrix of  slope values%}
dX=ones(size(dY));%{creates a matrix of ones the same size as dY%}
L=sqrt(1+dY.^2); %{scaling the arrows%}
quiver(X,Y,dX./L,dY./L); %{drawing the arrows using the mesh-grid%}
axis tight;%{gets rid of unneeded white space%}
