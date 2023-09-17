from src.scenes.components.button import Button
from src import constants as c


class EvaluateModelButton(Button):
    """Button that launches the machine learning evaluation graph."""

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self._create_button(0.5, 0.75, 300, 100, "Evaluate")

    def _activate(self) -> None:
        """Execute button function."""
        self._emitter = c.EVALUATE_MODEL_SCENE_INDEX
