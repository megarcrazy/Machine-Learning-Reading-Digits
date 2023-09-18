from typing import List
import matplotlib.pyplot as plt


class Graph:
    """
    Create a graph plotting number of training data from the storage used
    in the model vs accuracy.
    """

    def draw_graph(data_x: List[str], data_y: List[str]) -> None:
        """Draw graph with number of data vs accuracy."""
        plt.figure("Number of Data vs Accuracy")
        plt.plot(data_x, data_y)
        plt.gca().set_ylim(top=1)
        plt.xlabel("Number of Data")
        plt.ylabel("Accuracy")
        plt.title("Number of Data vs Accuracy")
        plt.show()
