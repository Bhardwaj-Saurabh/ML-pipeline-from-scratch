from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

from abc import ABC, abstractmethod

class Model(ABS):
    _model: None 

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value) -> None:
        self._model = value

    @abstractmethod
    def train(self, X: "pd.DataFrame", y: "pd.DataFrame") -> None:
        pass

    @abstractmethod
    def evaluate(self) -> None:
        pass

    @abstractmethod
    def create_report(self, artifact_path: str) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
        pass