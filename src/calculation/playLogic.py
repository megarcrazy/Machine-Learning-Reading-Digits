from typing import Tuple
from src.calculation.logic import Logic


class PlayLogic(Logic):
    """Class which handles backend logic of the Play Scene."""

    def __init__(self):
        super().__init__()
        self._playing = True
        self._prediction = None, None
        self._make_model()
        self._model.fit_model()
        self._reset_data()
        self._predict()
        self._loaded = False

    def update(self) -> None:
        """Detect user input."""
        if self._loaded:
            self._request_draw()
            self._request_submit_drawing()
        else:
            if self._await_mouse_lift():
                self._loaded = True

    def get_prediction(self) -> Tuple[int, float]:
        """
        Get current prediction of the input canvas data using the machine
        learning model. First index is number and second is probability.
        """
        return self._prediction

    def _submit_array(self) -> None:
        """Method to run when the user presses the "Submit Canvas" hotkey."""
        self._predict()
