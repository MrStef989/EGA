from abc import ABC, abstractmethod
from genetic.Individual import Individual

class MutationMethod(ABC):
    @abstractmethod
    def mutate(self, individual: Individual):
        pass
