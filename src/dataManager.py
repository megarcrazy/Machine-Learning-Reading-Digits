import numpy as np
from src.dataTransformer import DataTransformer


class DataManager:

    # Dump data into text file
    @staticmethod
    def dump_data(new_data):
        canvas = new_data[:-1]
        answer = new_data[-1]
        canvas = DataTransformer.centre_canvas(canvas)
        location = "src/data/data.csv"
        with open(location, "a") as f:
            np.savetxt(f, [canvas + [answer]], fmt="%i", delimiter=",")

    # Grab data from data storage file
    @staticmethod
    def get_data():
        location = "data/data.csv"
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
