import numpy as np
import os.path
import struct
import matplotlib.pyplot as plt

def read_nparray_binary(filename)
    """
    Read binary file and unpack using struct.unpack
    
    The file contains 3 doubles and is in big-endian format (>)
    
    :param filename: 
    :return: a 2d numpy array
    """



def plot_data(x,y,filename):
    """
    Plot data using matplotlib

    :param x:
    :param y:
    :param filename:
    :return:
    """


if __name__ == '__main__':
    binary_array = read_nparray_binary("filename goes here")
    plot_data(binary_array[:, 0], binary_array[:, 1], os.path.join("figures", "sin.png"))
    plot_data(binary_array[:, 0], binary_array[:, 2], os.path.join("figures", "cosine.png"))

