import sympy as sp
x = sp.Symbol('x')

print(sp.integrate(x**3,x))

from scipy.integrate import quad
def f(x):
    return  x**3
i=quad(f,0,10)
print(i)

