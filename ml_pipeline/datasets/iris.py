from typing import List

from ml_pipeline.dataset import Dataset
from ml_pipeline.mixins.csv_mixin import CSVMixin

class IrisDataset(CSVMixin, Dataset):
    """The Iris dataset.

    Source:
        https://archive.ics.uci.edu/ml/datasets/Iris

    Data Attributes:
        1. Sepal length in cm
        2. Sepal width in cm
        3. Petal length in cm
        4. Petal width in cm
        5. Class: {Iris setosa, Iris versicolour, Iris virginica}
    """
    def __init__(self, data_path: str) -> None:
        """Instantiates the dataset object.

        Args:
            data_path (str): Path to the CSV file.
        """
        self.name = "iris"
        self.data_path = data_path
        self.columns = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "species",
        ]

    def preprocess(self) -> None:
        """
        Preprocesses data
        """
        # preprocess the selected columns
        columns = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
        ]
        self.df[columns] = (
            self.df[columns] - self.df[columns].mean()
        )/self.df[columns].std()

    def feature_engineer(self, features: List[str]) -> List[str]:
        """Feature-engineer data.

        Args:
            features (List[str]): List of features to be used in training.
        Returns:
            List[str]: Updated list of features to be used in training.
        """
        self.df["sepal_area"] = (
            self.df["sepal_length"].abs() * self.df["sepal_width"].abs()
        )
        self.df["petal_area"] = (
            self.df["petal_length"].abs() * self.df["petal_width"].abs()
        )
        # return tha list with original and new features
        return features + ["sepal_area", "petal_area"]



