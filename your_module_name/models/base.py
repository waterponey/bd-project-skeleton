"""Model class, to be extended by specific types of models."""

class Model:
    """Base class, to be subclassed by predictors for specific type of data."""
    def __init__(self, dataset_cls: type, network_fn: Callable, dataset_args: Dict = None, network_args: Dict = None):

    @property
    def model_filename(self) -> str:
        return ...

    def fit(self, dataset, ...):

    def evaluate(self, x, y, ...):
        return ...

    def loss(self):
        return ...

    def optimizer(self):
        return ...

    def metrics(self):
        return ...

    def load_model(self):

    def save_model(self):
        
