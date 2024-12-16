from typing import List
from genetic.Individual import Individual

class CrossoverMethod:
    def crossover(self, individuals: List[Individual]) -> List[Individual]:
        raise NotImplementedError("This method must be implemented by subclasses.")
