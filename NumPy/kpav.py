from sympy import Symbol, integrate, sin, cos, exp

x = Symbol('x')
print(integrate(exp**(-x**2), x))