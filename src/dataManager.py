from typing import List, Tuple
import numpy as np
from src.dataTransformer import DataTransformer
import src.constants as c


class DataManager:
    def dump_data(new_data: List[int]) -> None:
        """Save single training data into text file."""
        canvas = new_data[:-1]
        answer = new_data[-1]  # Training data target is the last index
        canvas = DataTransformer.centre_canvas(
            canvas, c.TILE_X_AMOUNT, c.TILE_Y_AMOUNT
        )  # Remove offset variance
        data_location = "src/data/data.csv"
        with open(data_location, "a") as f:
            np.savetxt(f, [canvas + [answer]], fmt="%i", delimiter=",")

    def get_data() -> List[List[int]]:
        """Get training data from data storage file."""
        location = "src/data/data.csv"
        data = np.genfromtxt(location, delimiter=",")
        return data

    def convert_data(data) -> Tuple[List[int], List[int]]:
        """
        Converts data from data storage file and converts it into the sklearn
        format.
        """
        x, y = [], []  # x: input variables, y: target variables
        for array in data:
            x.append(array[:-1])
            y.append(array[-1])
        return x, y
