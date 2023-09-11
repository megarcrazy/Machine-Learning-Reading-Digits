from src.calculation.logic import Logic
from src.dataManager import DataManager


class TrainLogic(Logic):
    def __init__(self):
        super().__init__()
        self._reset_data()
        self._loaded = False

    def update(self):
        if self._loaded:
            self._request_draw()
            self._request_submit_drawing()
        else:
            if self._await_mouse_lift():
                self._loaded = True

    def _submit_array(self):
        DataManager.dump_data(self._data)
        self._reset_data()
