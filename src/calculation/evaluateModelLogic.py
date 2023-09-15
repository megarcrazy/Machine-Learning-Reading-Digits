from src.calculation.logic import Logic


class EvaluateModelLogic(Logic):
    """Class which handles backend logic of the Evaluate Model Scene."""

    def __init__(self):
        super().__init__()
        self._make_model()
        self._model.evaluate_accuracy()
