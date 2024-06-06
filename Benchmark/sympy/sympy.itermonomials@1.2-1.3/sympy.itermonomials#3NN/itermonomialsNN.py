from sympy import symbols, itermonomials
(x, y) = symbols('x y')
monomials = itermonomials(variables=[x, y], degree=2)
