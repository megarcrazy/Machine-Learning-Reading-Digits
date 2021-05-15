import matplotlib.pyplot as plt


class Graph:

    @staticmethod
    def draw_graph(data_x, data_y):
        plt.figure("Number of Data vs Accuracy")
        plt.plot(data_x, data_y)
        plt.gca().set_ylim(top=1)
        plt.xlabel("Number of Data")
        plt.ylabel("Accuracy")
        plt.title("Number of Data vs Accuracy")
        plt.show()
