% phase speed has a function of kDx for the physical and computational
% brances of CTCS

l = 2:6;
c = 0.4;
dx = 0.1;
dt = 0.1;
u = c*dx/dt;
k = 2*pi./(l*dx);

upbyu = 1./(k*dt*u).*asin(c*sin(k*dx));
ucbyu = -(pi + asin(c*sin(k*dx)))./(k*dt*u);

plot(l, upbyu, 'k', 'linewidth', 2, l, ucbyu, 'k--', 'linewidth', 2);
legend('physical mode', 'computational mode', 'location', 'east');
set(gca, 'linewidth', 1, 'position', [0.13 0.2 0.8 0.7]);
set(gca, 'tickdir', 'out', 'ticklength', [0.005 0.01]);
axis([2,6,-8,1]);
hold on
plot(l, zeros(size(l)), 'k:', 'linewidth', 1);
hold off
set(gcf, 'paperposition', [0.25 0.25 4 2.5]);
xlabel('wavelength/\Delta x')
ylabel('phase speed ratio')

print('CTCSphaseSpeed.eps')
system('epstopdf CTCSphaseSpeed.eps')

