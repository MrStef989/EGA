import random
from typing import List
from genetic.Individual import Individual
from methods.selection import SelectionMethod

class RandomSelection(SelectionMethod):
    def __init__(self):
        self.random = random.Random()

    def select_parents(self, population: List[Individual], number_of_parents: int) -> List[Individual]:
        parents = []
        for _ in range(number_of_parents):
            random_individual = population[self.random.randint(0, len(population) - 1)]
            parents.append(random_individual)
        return parents
