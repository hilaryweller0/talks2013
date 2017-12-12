# Find an approximate solution to
# x^5 + x + 1 = 0 using the 
# Bisection Method

# The function, f, we are solving
f = lambda x: x**5 + x + 1

# Set initial bounds, required
# error and a limit on the number
# of iterations
a = -1.0
b = 1.0
e = 1e-6
nmax = 100

# The iteration number for each
# iteration and the estimation for
# each iteration
it = 0
c = 0.5*(a+b)

# For efficiency, store the
# function evaluations so they
# don't need recaclulating
fa = f(a)
fb = f(b)
fc = f(a)

# Iterate until the solution is
# within the error limit or too
# many iterations
while abs(fc) > e and it < nmax:
    c = 0.5*(a+b)
    fc = f(c)
    if fa*fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc
    it += 1

print 'After ', it, ' iterations ',\
     'root = ', c, ' error = ', fc

