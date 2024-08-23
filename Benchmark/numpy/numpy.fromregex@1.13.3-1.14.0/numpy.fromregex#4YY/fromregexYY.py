import numpy as np
result = np.fromregex(file='./data.txt', regexp='(\\d+), (\\d+)', dtype=[('num1', int), ('num2', int)])
