from calculation.logic import Logic


class PlayLogic(Logic):

    def __init__(self):
        super().__init__()
        self._prediction = None, None
        self._make_model()
        self._model.fit_model()
        self._reset_data()
        self._predict()
        self._loaded = False

    def update(self):
        if self._loaded:
            self._request_draw()
            self._request_submit_drawing()
        else:
            if self._await_mouse_lift():
                self._loaded = True

    def get_prediction(self):
        return self._prediction

    def _submit_array(self):
        self._predict()
