from typing import List
from genetic.Individual import Individual
from items.Item import Item

class ConstraintStrategy:
    def enforce_constraints(self, individual: Individual, items: List[Item]) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")
