from math import sin, cos, pi
import matplotlib.pyplot as plt

#an explanation of the constants can be found in the
# fourier_transform_optimised.py file

s = 50000
iter8 = range(1, s+1)
L = -2
U = 2
f_L = 1
f_U = 10
T = U-L
w = 2*pi/T
width = T/s
def function(x):
    """
    the function to transform
    """
    return x**2 + x

def sin_int(n):
    """
    sin constants integrator
    """
    w_n = n*w
    area = 0
    for i in iter8:
        val = -(T/2) + T*i/s
        y = function(val)*sin(w_n*val)
        area+=y
    return area*width*2/T

def cos_int(n):
    """
    cos constants integrator
    """
    w_n = n*w
    area = 0
    for i in iter8:
        val = -(T/2) + T*i/s
        y = function(val)*cos(w_n*val)
        area+=y
    return area*width*2/T


def fourier_transform():
    C_0 = 0
    for i in iter8:
        val = -(T/2) + T*i/s
        C_0+=function(val)
    C_0*=width*2/T
    C = []
    S = []
    for i in range(f_L, f_U+1):
        C_val = cos_int(i)
        S_val = sin_int(i)
        if abs(C_val) <= 10**-14:
            C_val = 0
        if abs(S_val) <= 10**-14:
            S_val = 0
        C.append(round(C_val, 6))
        S.append(round(S_val, 6))
    return(C_0, S, C)

def plot_fouriers():
    nums = 5000
    vals = fourier_transform()
    C_0 = vals[0]
    S = vals[1]
    C = vals[2]
    plot_vals = [[], []]
    true_vals = [[], []]
    def fourier_approx(x):
        y = C_0/2
        for i in range(1, (1+f_U-f_L)):
            w_n = i*w
            y+= S[i-1]*sin(w_n*x)+ C[i-1]*cos(w_n*x)
        return y
    for i in range(0, nums):
        val = L + i*T/nums
        plot_vals[0].append(val)
        true_vals[0].append(val)
        plot_vals[1].append(fourier_approx(val))
        true_vals[1].append(function(val))
    print(plot_vals)
    plt.plot(plot_vals[0], plot_vals[1])
    plt.plot(true_vals[0], true_vals[1])
