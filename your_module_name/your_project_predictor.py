"""CharacterPredictor class"""
from typing import Tuple, Union

import numpy as np

from your_module_name.models import YourModel



class YourPredictor:
    def __init__(self):
        self.model = YourModel()
        self.model.load_weights()

    def predict(self, x)
        ...
        return self.model.predict(x)

    def evaluate(self, dataset):
        return self.model.evaluate(dataset.x_test, dataset.y_test)
