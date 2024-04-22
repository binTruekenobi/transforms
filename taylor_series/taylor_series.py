import polynomial_tools as pt
from math import exp
width = 10**-3

"""
often the best value of the derivative can be found 
with d between 10**-8 and 10**-11, as the 
accuracy the floats are stored at begins to change the
value calculated

nvm use 10**-3 or it goes wack

things to do:
    
1. add algebra to get sum of constant * (x-a)^n in terms of just x^n done
2. find the L(t^n) formula L(t^n) = n!/(s^(n+1))
3. figure out how to get a common denominator working
plumbing
bunch up the wires and chuck them in the laplace
transform calculator so it estimates the function
then laplace transforms
then figure out how to get some plots
plot real and imaginary on different axes or use sympy
"""

def factorial(n):
    if n<2:
        return 1
    """
    replace with rt(5) formula
    """
    x=1
    for i in range(2, n+1):
        x*=i
    return x

def pascal_signs_gen(n):
    x = []
    f_n = factorial(n)
    for i in range(0, n+1):
        x.append((-1)**(i%2)*(f_n/(factorial(i)*factorial(n-i))))
    return x

def constants(n):
    x = [factorial(n)/(factorial(n-i)*factorial(i)) for i in range(0, n+1)]
    return x

def binom(n, k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def maclaurin(function, terms, show_taylor = True, rnd = 6):
    inv_width = 10**3
    derivs = []
    for i in range(1, int(terms+1)):
        #print(i)
        weights = pascal_signs_gen(i)
        s = 0
        for j in range(0, i+1):
            val = (j-i/2)*width
            #print(val)
            f_val = function(val)
            #print(f_val)
            w_f_val = weights[j]*f_val
            s+=w_f_val
        derivative = s*(inv_width**i)*(-1)**((i)%2)/factorial(i)
        derivs.append(round(derivative, rnd))
    derivs = [round(function(0), rnd)] + derivs
    print(derivs)
    if not show_taylor:
        return derivs
    else:
        k = [float(derivs[i]) for i in range(int(terms), -1, -1)]
        j = pt.polynomial(k)
        return print(j)


def taylor(function, x, terms, show_taylor = True, rnd = 6, simplify=True):
    if x == 0:
        return maclaurin(function, terms, show_taylor=show_taylor, rnd=rnd)
    inv_width = 10**3
    derivs = []
    for i in range(1, terms+1):
        #print(i)
        weights = pascal_signs_gen(i)
        s = 0
        for j in range(0, i+1):
            val = x + (j-i/2)*width
            #print(val)
            f_val = function(val)
            #print(f_val)
            w_f_val = weights[j]*f_val
            s+=w_f_val
        derivative = s*(inv_width**i)*(-1)**((i)%2)/factorial(i)
        derivs.append(round(derivative, rnd))
    derivs = [round(function(x), rnd)] + derivs
    print(derivs)
    if not show_taylor:
        return derivs
    else:
        k = [float(derivs[i]) for i in range(terms, -1, -1)]
        j = pt.polynomial_shift(k, x)
        print(j)
    if simplify:
        consts = []
        for i in range(0, terms+1):
            vals = derivs[i:]
            const=0
            for j in range(i, terms+1):
                c1 = float(vals[j-i])
                c2 = binom(j, i)
                c3 = (float(-x)**(j-i))
                const+=c1*c2*c3
            consts.append(round(const, rnd))
        #k = [round(consts[i], rnd) for i in range(terms, -1, -1)]
        #j = pt.polynomial(k)
        #print(j)
        return consts
    return
