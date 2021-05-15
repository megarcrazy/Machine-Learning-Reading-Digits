from calculation.logic import Logic


class EvaluateModelLogic(Logic):

    def __init__(self):
        super().__init__()
        self._make_model()
        self._model.evaluate_accuracy()
