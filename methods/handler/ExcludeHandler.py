from typing import List
from genetic.Individual import Individual
from items.Item import Item
from methods.handler.ConstraintStrategy import ConstraintStrategy
class ExcludeHandler(ConstraintStrategy):
    def __init__(self, max_weight: float):
        self.max_weight = max_weight

    def enforce_constraints(self, individual: Individual, items: List[Item]) -> None:
        if individual.get_weight > self.max_weight:
            print(f"Особь исключена: Генотип: {individual.get_genotype} | Вес: {individual.get_weight:.2f} | Приспособленность: {individual.get_fitness:.2f}")
            individual.fitness = 0.0
