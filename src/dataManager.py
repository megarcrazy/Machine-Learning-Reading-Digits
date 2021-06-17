import ast
import numpy as np


class DataManager:

    # Dump data into text file
    @staticmethod
    def dump_data(new_data):
        location = "src/data/data.csv"
        print(type(new_data))
        with open(location, "a") as f:
            np.savetxt(f, [new_data], fmt="%i", delimiter=",")

    # Grab data from data storage file
    @staticmethod
    def get_data():
        location = "src/data/data.csv"
        data = np.genfromtxt(location, delimiter=",")
        return data

    # Converts data from data storage file and converts it into the sklearn
    # format.
    @staticmethod
    def convert_data(data):
        x, y = [], []
        for array in data:
            x.append(array[:-1])
            y.append(array[-1])
        return x, y
