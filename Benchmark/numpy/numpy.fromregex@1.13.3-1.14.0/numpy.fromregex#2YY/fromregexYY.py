import numpy as np
result = np.fromregex('./data.txt',  '(\\d+), (\\d+)', dtype=[('num1', int), ('num2', int)])
