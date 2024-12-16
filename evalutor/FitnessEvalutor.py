from typing import List
from genetic.Individual import Individual  # Предполагается, что класс Individual уже определен
from items.Item import Item # Предполагается, что класс Item уже определен

class FitnessEvalutor:
    def __init__(self):
        pass

    def evaluate(self, individuals: List[Individual], items: List[Item], max_weight: float):
        for individual in individuals:
            individual.calculate_characteristics(items, max_weight)
