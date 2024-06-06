import numpy as np

def main():
    a = np.array([1, 2, 3])
    v = np.array([0, 1, 0.5])
    result = np.correlate(a,  v, mode='valid', old_behavior=False)
    print(result)
if __name__ == '__main__':
    main()
