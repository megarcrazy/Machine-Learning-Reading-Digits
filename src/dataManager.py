import ast


class DataManager:

    # Dump data into text file
    @staticmethod
    def dump_data(new_data):
        location = "data/data.txt"
        with open(location, "a") as f:
            f.write(str(new_data) + "\n")

    # Grab data from data storage file
    @staticmethod
    def get_data():
        location = "data/data.txt"
        with open(location, "r") as f:
            text = f.read()
            data = [ast.literal_eval(array) for array in text.split("\n")[:-1]]
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
