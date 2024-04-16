from math import sin, cos, pi
import matplotlib.pyplot as plt
from numpy import empty, linspace, sum

"""
constants:

s = number of chops the integrators use
L = lower bound of the function's period
U = upper bound of the function's period
f_L = lowest frequency in the transform
f_U = highest frequency in the transform
round_S/C = rounding on the fourier series 

treat_as_0_S/C = fourier series values which can be treated as 0,
for even/odd functions all sin/cos values may be 0, but will be
something close to 10**-16 instead due to rounding, so 
when the series is returned this can be rounded to 0 instead

nums is the number of chops the graph uses for the approximate 
values to plot in the plot_fouriers function,
in this file this number does not affect the resolution of the 
plot of the actual function, as they are calculated using 
s slices already so it doesn't bother re-calculating them,
nums does affect the actual function plot in the
fourier_transform_function.py file as values are not already known
"""

s = 100000
L = -2
U = 2
iter8 = linspace(L, U, s)
lin = linspace(0, s-1, s, dtype=int)
f_L = 1
f_U = 200
acc = 1+f_U - f_L
T = U-L
w = 2*pi/T
width = T/s
acc8 = linspace(1, acc, acc, dtype=int)
round_S = 8
round_C = 8
treat_as_0_S = 10**-14
treat_as_0_C = 10**-14
nums = 5000

def function(x):
    return x**2+x

f_vals = empty(s)
for i in lin:
    f_vals[i] = function(iter8[i])
    
def sin_int(n):
    w_n = n*w
    area = 0
    for i in lin:
        area+=function(iter8[i])*sin(w_n*iter8[i])
    return area*width*2/T

def cos_int(n):
    w_n = n*w
    area = 0
    for i in lin:
        area+=function(iter8[i])*cos(w_n*iter8[i])
    return area*width*2/T


def fourier_transform():
    C_0 = sum(f_vals)*width*2/T
    C = empty(acc)
    S = empty(acc)
    for i in range(f_L, f_U+1):
        C_val = cos_int(i)
        S_val = sin_int(i)
        if abs(C_val) <= treat_as_0_C:
            C_val = 0
        if abs(S_val) <= treat_as_0_S:
            S_val = 0
        C[i-f_L] = round(C_val, round_C)
        S[i-f_L] = round(S_val, round_S)
    return(C_0, S, C)

def plot_fouriers():
    p = linspace(L, U, nums)
    pl = linspace(0, nums-1, nums, dtype=int)
    vals = fourier_transform()
    C_0 = vals[0]
    S = vals[1]
    C = vals[2]
    plot_vals = empty(nums)
    def fourier_approx(x):
        y = C_0/2
        for i in range(1, (1+f_U-f_L)):
            w_n = i*w
            y+= S[i-1]*sin(w_n*x)+ C[i-1]*cos(w_n*x)
        return y
    for i in pl:
        plot_vals[i] = fourier_approx(p[i])
    plt.plot(p, plot_vals)
    plt.plot(iter8, f_vals)
