from typing import List
from genetic.Individual import Individual
from items.Item import Item
from utilis import Utils
from methods.handler.ConstraintStrategy import ConstraintStrategy


class GenotypeModifier(ConstraintStrategy):
    def __init__(self, max_weight: float):
        self.max_weight = max_weight

    def enforce_constraints(self, individual: Individual, items: List[Item]) -> None:
        current_weight = individual.get_weight
        if current_weight > self.max_weight:
            genotype = individual.get_genotype
            mutated_genotype = list(genotype)  # Преобразуем строку в список символов для изменения
            sorted_indices = Utils.get_sorted_indices_by_value_to_weight_ratio(items, genotype)

            print(f"Изначальный генотип (до исправления): {genotype} | Вес: {current_weight:.2f}")

            for index in sorted_indices:
                if current_weight <= self.max_weight:
                    break

                if mutated_genotype[index] == '1':
                    mutated_genotype[index] = '0'
                    current_weight -= items[index].get_weight()

            mutated_genotype_str = ''.join(mutated_genotype)
            print(f"Генотип после исправления: {mutated_genotype_str} | Новый вес: {current_weight:.2f}")

            individual.genotype = mutated_genotype_str
            individual.calculate_characteristics(individual.get_items, individual.get_max_weight)
