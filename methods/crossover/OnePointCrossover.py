import random
from typing import List
from genetic.Individual import Individual


class OnePointCrossover:
    def __init__(self):
        self.random = random.Random()

    def crossover(self, parents: List[Individual]) -> List[Individual]:
        if len(parents) != 2:
            raise ValueError("OnePointCrossover требует ровно 2 родителей.")

        parent1 = parents[0]
        parent2 = parents[1]

        genotype1 = parent1.get_genotype
        genotype2 = parent2.get_genotype

        if len(genotype1) != len(genotype2):
            raise ValueError("Генотипы родителей должны иметь одинаковую длину.")

        offspring = []
        genotype_length = len(genotype1)

        # Генерируем случайные точки кроссовера
        crossover_point1 = self.random.randint(1, genotype_length - 1)
        crossover_point2 = self.random.randint(1, genotype_length - 1)
        crossover_point3 = self.random.randint(1, genotype_length - 1)

        # Создаем потомков
        child_genotype1 = genotype1[:crossover_point1] + genotype2[crossover_point1:]
        offspring.append(Individual(child_genotype1, parent1.get_items, parent1.get_max_weight))

        child_genotype2 = genotype2[:crossover_point2] + genotype1[crossover_point2:]
        offspring.append(Individual(child_genotype2, parent1.get_items, parent1.get_max_weight))

        child_genotype3 = genotype1[:crossover_point3] + genotype2[crossover_point3:]
        offspring.append(Individual(child_genotype3, parent1.get_items, parent1.get_max_weight))

        return offspring
