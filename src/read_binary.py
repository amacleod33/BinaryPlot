import numpy as np
import os.path
import struct
import matplotlib.pyplot as plt

def read_nparray_binary(filename):
    """
    Read binary file and unpack using struct.unpack
    
    The file contains 3 doubles and is in big-endian format (>)
    
    :param filename: 
    :return: a 2d numpy array
    """

    with open(filename, 'rb') as file:
        ba = bytearray(file.read())

    chunk_size = struct.calcsize('>ddd')
    num_array = []

    for i in range(len(ba)//chunk_size):
        data = struct.unpack('>ddd', ba[i*chunk_size:(i + 1)*chunk_size])
        num_array.append(list(data))
    return np.array(num_array)



def plot_data(x,y,filename, title):
    """
    Plot data using matplotlib

    :param x:
    :param y:
    :param filename:
    :return:
    """

    with open(filename, 'w+') as file:
        plt.xkcd()
        plt.plot(x, y)
        plt.xlabel('X Values')
        plt.ylabel('Y Values')

        plt.title(title)
        plt.show()

def plot_both(w, x, y, z, filename1, filename2):
    with open(filename1, 'w+') as file:
        plt.plot(w, x, label='sine')
        plt.plot(y, z, label='cosine')
        plt.title('Sin and cosine')
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        plt.legend(loc='upper left')
        plt.show()

if __name__ == '__main__':
    dat_file = os.path.join('data', 'test_data.dat')
    binary_array = read_nparray_binary(dat_file)
    plot_data(binary_array[:, 0], binary_array[:, 1], os.path.join("figures", "sin.png"), 'Sine')
    plot_data(binary_array[:, 0], binary_array[:, 2], os.path.join("figures", "cosine.png"), 'Cosine')
    plot_both(binary_array[:, 0], binary_array[:, 1], binary_array[:, 0], binary_array[:, 2], os.path.join('figures', 'cosine.png'), os.path.join('figures', 'sine.png'))
