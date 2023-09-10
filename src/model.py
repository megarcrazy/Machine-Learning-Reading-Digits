import joblib
from src.dataTransformer import DataTransformer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.scenes.graph import Graph


class Model:

    def __init__(self, data=None, playing=False):
        # Uses data from local database to produce a model
        self._x, self._y = data
        self._model = SVC
        self._clf = self._model(gamma=0.1, C=10)
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
        clf = model(gamma="auto")
        clf.fit(x_train, y_train)
        y_prediction = clf.predict(x_test)
        accuracy = accuracy_score(y_test, y_prediction)
        return accuracy

    # Get computer predicted number and probability
    def predict(self, fit_data):
        fit_data = [DataTransformer.centre_canvas(fit_data[0])]
        number = int(self._clf.predict(fit_data))
        probability = max(self._clf.predict_proba(fit_data)[0])
        return number, probability

    # Find optimal Gamma and C for the SVC model
    def _find_optimal_parameters(self):
        # Code from "Introduction toMachineLearning with Python by Andreas C. Müller & Sarah Guido"
        # page 306
        from sklearn.model_selection import GridSearchCV
        param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
        grid = GridSearchCV(SVC(), param_grid=param_grid, cv=5)
        grid.fit(self._x, self._y)
        print("Best cross-validation accuracy: {:.2f}".format(grid.best_score_))
        print("Best parameters: ", grid.best_params_)
