from abc import ABC, abstractmethod
from genetic.Individual import Individual
from typing import List
class SelectionMethod(ABC):
    @abstractmethod
    def select_parents(self, individuals: List[Individual], population_size: int) -> List[Individual]:
        pass
