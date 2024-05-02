from abc import ABC, abstractmethod

class PGM(ABC):
    """Abstract base class for Probabilistic Graphical Models."""

    def __init__(self, structure_and_weights=False):
        """
        Creates a new instance of the PGM class.

        Parameters: :param structure_and_weights: Indicates that the model is capable of learning the structure and
        weights together.
        """
        self.__structure_and_weights = structure_and_weights
        self.__fully_learned = False
        self.__structure_learned = False

    @abstractmethod
    def inference(self, query_variables):
        """Perform inference on the given query variables."""
        if not self.__fully_learned:
            raise RuntimeError("Illegal state: cannot do inference on a model where structure or weights is unknown.")

    @abstractmethod
    def sample(self, num_samples):
        """Sample from the model."""
        if not self.__fully_learned:
            raise RuntimeError("Illegal state: cannot sample from a model where structure or weights is unknown.")

    @abstractmethod
    def learn_weights(self, data):
        """Learn the parameters of the model from the given data."""

        if not self.__structure_learned and not self.__structure_and_weights:
            raise RuntimeError("Illegal state: please learn structure first.")

    @abstractmethod
    def learn_structure(self, data):
        """Learn the structure of the model from the given data."""
        pass