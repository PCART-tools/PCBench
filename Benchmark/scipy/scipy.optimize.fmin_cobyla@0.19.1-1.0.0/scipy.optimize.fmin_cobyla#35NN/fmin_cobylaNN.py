from scipy.optimize import fmin_cobyla

def objective(x):
    return x[0] ** 2 + x[1] ** 2
constraints = [lambda x: 1 - x[0] - x[1], lambda x: x[0] - 2 * x[1] - 3]
x0 = [0.5, 0.5]
rhobeg = 1.0
rhoend = 0.0001
iprint = 1
maxfun = 1000
disp = 1
catol = 0.0002
result = fmin_cobyla(objective,  x0,  constraints,  (), consargs=None, rhobeg=rhobeg, rhoend=rhoend, iprint=iprint)
