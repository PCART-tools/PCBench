from sympy import symbols, itermonomials
(x, y) = symbols('x y')
monomials = itermonomials([x, y], degree=2)
