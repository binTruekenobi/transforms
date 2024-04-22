import matplotlib.pyplot as plt

s = 1000
width = 1/s

def f(x):
    return x**2+x+1

def g(x):
    return x**3

def c_integral(val):
    total = 0
    for i in range(s):
        x = val*i/s
        f_val = f(x)
        g_val = g(val-x)
        prod = f_val*g_val
        total+=prod
    return total*width


def convolution(L, U, steps):
    x = []
    y = []
    for i in range(0, steps):
        val = L+i*(U-L)/steps
        #integrate f(x)*g(val-x) between 0 and val
        x.append(val)
        y.append(c_integral(val))
    plt.plot(x, y)
        
convolution(-1, 1, 50)