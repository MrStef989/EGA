import random
from typing import List
from genetic.Individual import Individual
from methods.selection import SelectionMethod

class RouletteWheelSelection(SelectionMethod):
    def __init__(self):
        self.random = random.Random()

    def select_parents(self, population: List[Individual], number_of_parents: int) -> List[Individual]:
        parents = []
        total_fitness = sum(individual.get_fitness for individual in population)

        for _ in range(number_of_parents):
            rand = self.random.random() * total_fitness
            cumulative = 0.0

            for individual in population:
                cumulative += individual.get_fitness
                if cumulative >= rand:
                    parents.append(individual)
                    break

        return parents
