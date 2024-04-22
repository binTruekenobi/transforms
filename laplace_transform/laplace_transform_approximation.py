import sys
sys.path.insert(0, r"insert the path to the taylor series file here")
sys.path.insert(0, r"insert the path to the polynomial tools file here")

from taylor_series import *
from math import sin, cos
from polynomial_tools import *

x = 1
terms = 5

def function(x):
    return sin(x)+cos(x)+(x**10)

"""
L(t^n) = n!/(s^(n+1))
"""

def unilateral_laplace():
    vals = taylor(function, x, terms, show_taylor = True, rnd = 6, simplify=True)
    consts = []
    for i in range(0, terms+1):
        const = factorial(i)*vals[i]
        consts.append(const)
    denom = terms+1
    j = polynomial(consts)
    string = j.__str__()
    return "("+string+")"+"/(s^("+str(denom)+"))"

unilateral_laplace()
