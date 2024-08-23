import numpy as np
result = np.fromregex('./data.txt',  '(\\d+), (\\d+)',  [('num1', int), ('num2', int)])
