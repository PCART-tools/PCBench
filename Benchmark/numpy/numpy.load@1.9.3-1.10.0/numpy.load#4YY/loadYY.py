import numpy as np

def main():
    loaded_data = np.load('./example.npy', mmap_mode=None)
    print(loaded_data)
if __name__ == '__main__':
    main()
