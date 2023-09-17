from src.calculation.logic import Logic
from src.dataManager import DataManager


class TrainLogic(Logic):
    """Class which handles backend logic of the Train Scene."""

    def __init__(self) -> None:
        super().__init__()
        self._reset_data()
        self._loaded = False

    def update(self) -> None:
        """Detect user input."""
        if self._loaded:
            self._request_draw()
            self._request_submit_drawing()
        else:
            if self._await_mouse_lift():
                self._loaded = True

    def _submit_array(self) -> None:
        """Method to run when the user presses the "Submit Canvas" hotkey."""
        DataManager.dump_data(self._data)
        # Clear canvas and generate a random number on the last index of
        # self._data
        self._reset_data()
