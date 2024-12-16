import random
from typing import List
from genetic.Individual import Individual


class TwoPointCrossover:
    def __init__(self):
        self.random = random.Random()

    def crossover(self, parents: List[Individual]) -> List[Individual]:
        if len(parents) != 2:
            raise ValueError("TwoPointCrossover требует ровно 2 родителей.")

        parent1 = parents[0]
        parent2 = parents[1]

        genotype1 = parent1.get_genotype
        genotype2 = parent2.get_genotype

        if len(genotype1) != len(genotype2):
            raise ValueError("Генотипы родителей должны иметь одинаковую длину.")

        offspring = []
        genotype_length = len(genotype1)

        for _ in range(3):  # создаем 3 потомков
            point1 = self.random.randint(1, genotype_length - 1)

            point2 = self.random.randint(1, genotype_length - 1)
            while point1 == point2:
                point2 = self.random.randint(1, genotype_length - 1)

            # Обеспечиваем, чтобы point1 был меньше point2
            if point1 > point2:
                point1, point2 = point2, point1

            # Создаем потомка, комбинируя генотипы родителей
            child_genotype = genotype1[:point1] + genotype2[point1:point2] + genotype1[point2:]
            offspring.append(Individual(child_genotype, parent1.get_items, parent1.get_max_weight))

        return offspring
