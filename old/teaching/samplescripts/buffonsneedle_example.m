%assume the needle is of unit length.
%floor cracks are 2 units apart.
clear;

c = struct('rr', [0.7, 0.0, 0.0], 'bb', [0,0,.7]); %defining custom colors. 

n=10000000; %set the number of needles

r_1=2*rand(n,2)-1; %generates random endpoints of needle in [-1,1]x[-1,1].

theta=2*pi*rand(n,1); %generates random rotation angle for needle. 

r_2=r_1+[cos(theta),sin(theta)]; %find the other endpoint one unit length away at the angle theta. 

% Helps find sign changes.
s=r_1.*r_2; 

%plotting the first 500 needles and 'floorboard crack'.
for i=1:min(500,n)
    axis([-2 2 -2 2]);
    plot([-2;2],[0;0],'black' ,'Linewidth',2);
    title('Plot of the first 500 (or under) needles.')
    if s(i,2)<0
        %red needle if it crosses.
        plot([r_1(i,1); r_2(i,1)],[r_1(i,2);r_2(i,2)], 'Color', c.rr);
        hold on;
    else
        %blue needle if it doesnt cross.
        plot([r_1(i,1); r_2(i,1)],[r_1(i,2);r_2(i,2)], 'Color', c.bb);
        hold on;
    end

end



%calculating pi from the number of crossings. 
S=sign(s);
final_crossings=sum(S(1:end,2)==-1);
final_approx=n/final_crossings;
