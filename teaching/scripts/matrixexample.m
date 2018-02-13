A=[.5,-.6;.75,1.1]; 
x=[2;0];
for n= 1:100
    x= A*x;
    disp(x);
    hold on;
    plot (x(1),x(2), 'sk');
end
