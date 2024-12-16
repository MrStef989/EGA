import random
from typing import List
from genetic.Individual import Individual


class UniformCrossover:
    def __init__(self):
        self.random = random.Random()

    def crossover(self, parents: List[Individual]) -> List[Individual]:
        if len(parents) != 2:
            raise ValueError("UniformCrossover требует ровно 2 родителей.")

        parent1 = parents[0]
        parent2 = parents[1]

        genotype1 = parent1.get_genotype
        genotype2 = parent2.get_genotype

        if len(genotype1) != len(genotype2):
            raise ValueError("Генотипы родителей должны иметь одинаковую длину.")

        offspring = []

        for _ in range(3):  # создаем 3 потомков
            child_genotype = []

            for i in range(len(genotype1)):
                from_parent1 = self.random.choice([True, False])  # Случайно выбираем родителя
                gene = genotype1[i] if from_parent1 else genotype2[i]
                child_genotype.append(gene)

            # Создаем потомка с новым генотипом
            offspring.append(Individual("".join(child_genotype), parent1.get_items, parent1.get_max_weight))

        return offspring
