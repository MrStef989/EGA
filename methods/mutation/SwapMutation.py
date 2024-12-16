import random
from genetic import Individual
from methods.mutation import MutationMethod

class SwapMutation(MutationMethod):
    def __init__(self, mutation_rate: float):
        self.mutation_rate = mutation_rate
        self.random = random.Random()

    def mutate(self, individual: Individual):
        if self.random.random() < self.mutation_rate:
            genotype = list(individual.get_genotype)  # Преобразуем строку в список
            length = len(genotype)
            if length < 2:
                return

            index1 = self.random.randint(0, length - 1)
            index2 = self.random.randint(0, length - 1)

            # Обмен значениями на позициях index1 и index2
            genotype[index1], genotype[index2] = genotype[index2], genotype[index1]

            # Возвращаем генотип обратно в строку
            mutated_genotype = ''.join(genotype)
            individual.genotype=mutated_genotype
