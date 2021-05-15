from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.scenes.graph import Graph


class Model:

    def __init__(self, data=None):
        self._x, self._y = data
        self._model = SVC
        self._clf = self._model()
        self._clf = CalibratedClassifierCV(self._clf)

    def fit_model(self):
        self._clf.fit(self._x, self._y)

    # Calculates the predicted accuracy of the model by using the stored data
    # and splitting the data into training and testing data
    def evaluate_accuracy(self):
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
    def _get_accuracy(x, y, model):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        clf = model()
        clf.fit(x_train, y_train)
        y_prediction = clf.predict(x_test)
        accuracy = accuracy_score(y_test, y_prediction)
        return accuracy

    # Get computer predicted number and probability
    def predict(self, fit_data):
        number = int(self._clf.predict(fit_data))
        probability = max(self._clf.predict_proba(fit_data)[0])
        return number, probability
