import random
from genetic import Individual
from methods.mutation import MutationMethod

class InversionMutation(MutationMethod):
    def __init__(self, mutation_rate: float):
        self.mutation_rate = mutation_rate
        self.random = random.Random()

    def mutate(self, individual: Individual):
        if self.random.random() < self.mutation_rate:
            genotype = individual.get_genotype
            length = len(genotype)
            if length < 2:
                return

            point1 = self.random.randint(0, length - 1)
            point2 = point1 + self.random.randint(0, length - point1)
            mutated_genotype = list(genotype)

            for i in range(point1, point2):
                current_bit = mutated_genotype[i]
                inverted_bit = '1' if current_bit == '0' else '0'
                mutated_genotype[i] = inverted_bit

            mutated_genotype_str = ''.join(mutated_genotype)
            individual.genotype=mutated_genotype_str
