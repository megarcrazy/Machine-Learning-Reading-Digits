from typing import Tuple, List
import sklearn
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from src.scenes.graph import Graph
from src.dataTransformer import DataTransformer
import src.constants as c


class Model:
    """
    Machine learning model to fit on input data for training and
    non-training mode.
    """

    def __init__(
        self, data: Tuple[List[int], List[int]] = None, playing: bool = False
    ):
        self._x, self._y = data
        self._model = SVC
        self._clf = self._model(gamma=0.1, C=10)
        self._clf = CalibratedClassifierCV(self._clf)

    def fit_model(self):
        """Fit model on training data."""
        self._clf.fit(self._x, self._y)

    def evaluate_accuracy(self):
        """
        Calculates the predicted accuracy of the model by using the stored data
        and splitting the data into training and testing data.
        """
        intervals = 30
        amount_list = []
        accuracy_list = []
        for i in range(intervals):
            amount = int(len(self._x) / intervals * (i + 1))
            amount_list.append(amount)
            temp_x = self._x[:amount]
            temp_y = self._y[:amount]
            accuracy = self._get_accuracy(temp_x, temp_y, self._model)
            accuracy_list.append(accuracy)
        Graph.draw_graph(amount_list, accuracy_list)

    @staticmethod
    def _get_accuracy(
        x: List[int], y: List[int], model: sklearn.base.ClassifierMixin
    ):
        """Get accuracy of training data."""
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2
        )
        clf = model(gamma="auto")
        clf.fit(x_train, y_train)
        y_prediction = clf.predict(x_test)
        accuracy = accuracy_score(y_test, y_prediction)
        return accuracy

    def predict(self, fit_data: List[List[int]]):
        """Get computer predicted number and probability of input data."""
        fit_data = [
            DataTransformer.centre_canvas(
                fit_data[0], c.TILE_X_AMOUNT, c.TILE_Y_AMOUNT
            )
        ]
        number = int(self._clf.predict(fit_data))
        probability = max(self._clf.predict_proba(fit_data)[0])
        return number, probability

    def _find_optimal_parameters(self):
        """Find optimal Gamma and C for the SVC model."""
        param_grid = {
            "C": [0.001, 0.01, 0.1, 1, 10, 100],
            "gamma": [0.001, 0.01, 0.1, 1, 10, 100],
        }
        grid = GridSearchCV(SVC(), param_grid=param_grid, cv=5)
        grid.fit(self._x, self._y)
