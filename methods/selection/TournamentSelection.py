import random
from typing import List
from genetic.Individual import Individual
from methods.selection import SelectionMethod

class TournamentSelection(SelectionMethod):
    def __init__(self, tournament_size: int):
        self.tournament_size = tournament_size
        self.random = random.Random()

    def select_parents(self, population: List[Individual], number_of_parents: int) -> List[Individual]:
        parents = []
        for _ in range(number_of_parents):
            # Выбираем случайных участников для турнира
            tournament = [random.choice(population) for _ in range(self.tournament_size)]

            # Находим лучшего по приспособленности
            best = max(tournament, key=lambda individual: individual.get_fitness)  # Исправлено
            parents.append(best)
        return parents

