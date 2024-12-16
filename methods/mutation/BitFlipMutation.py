import random
from genetic.Individual import Individual
from methods.mutation.MutationMethod import MutationMethod
class BitFlipMutation(MutationMethod):
    def __init__(self, mutation_rate: float):
        self.mutation_rate = mutation_rate

    def mutate(self, individual: Individual) -> None:
        # Получаем генотип особи
        mutated_genotype = list(individual.get_genotype)  # Строка превращается в список для удобства изменения

        # Проходим по всем битам генотипа
        for i in range(len(mutated_genotype)):
            if random.random() < self.mutation_rate:
                # Переворачиваем бит ('1' -> '0' и наоборот)
                current = mutated_genotype[i]
                mutated_genotype[i] = '0' if current == '1' else '1'

        # Преобразуем изменённый генотип обратно в строку
        mutated_genotype_str = ''.join(mutated_genotype)

        # Обновляем генотип особи

        individual.genotype=mutated_genotype_str
