import random
from typing import List
from config import Config
from items.Item import Item
from genetic.Individual import Individual
from methods.selection import SelectionMethod
from utilis import Utils

class Population:
    def __init__(self, config: Config, items: List[Item]):
        if items and len(items) > 0:
            self.config = config
            self.size = config.get_population_size()
            self.items = items
            self.max_weight = config.get_max_weight()
            self.individuals: List[Individual] = []
            self.initialize_population()
        else:
            raise ValueError("Список предметов (items) не может быть null или пустым.")

    def initialize_population(self):
        strategy = self.config.get_initial_population_strategy()
        if strategy == "Hybrid":
            self.generate_hybrid_population()
        elif strategy == "Roulette":
            self.generate_roulette_population()
        else:
            self.generate_random_population()

    def generate_random_population(self):
        attempts = 0
        while len(self.individuals) < self.size:
            genotype = Utils.generate_valid_genotype(len(self.items), self.items, self.max_weight)
            individual = Individual(genotype, self.items, self.max_weight)
            if individual.weight > self.max_weight:  # Используем свойство вместо метода
                attempts += 1
                if attempts > self.size * 10:
                    raise RuntimeError("Слишком много попыток создать допустимую популяцию.")
                continue
            self.individuals.append(individual)

    def generate_hybrid_population(self):
        greedy_size = self.size // 2
        random_size = self.size - greedy_size

        # Генерация жадной части популяции
        attempts = 0
        for _ in range(greedy_size):
            while True:
                genotype = self.generate_randomized_greedy_genotype(self.items, self.max_weight)
                individual = Individual(genotype, self.items, self.max_weight)
                if individual.weight <= self.max_weight:  # Используем свойство вместо метода
                    self.individuals.append(individual)
                    break
                else:
                    attempts += 1
                    if attempts > greedy_size * 10:
                        raise RuntimeError("Слишком много попыток создать жадную часть популяции.")

        # Генерация случайной части популяции
        attempts = 0
        for _ in range(random_size):
            while True:
                genotype = Utils.generate_valid_genotype(len(self.items), self.items, self.max_weight)
                individual = Individual(genotype, self.items, self.max_weight)
                if individual.weight <= self.max_weight:  # Используем свойство вместо метода
                    self.individuals.append(individual)
                    break
                else:
                    attempts += 1
                    if attempts > random_size * 10:
                        raise RuntimeError("Слишком много попыток создать случайную часть популяции.")

    def generate_randomized_greedy_genotype(self, items: List[Item], max_weight: float) -> str:
        shuffled_items = items.copy()
        random.shuffle(shuffled_items)
        genotype = ['0'] * len(items)
        current_weight = 0.0

        for item in shuffled_items:
            if current_weight + item.get_weight() <= max_weight:
                index = self.items.index(item)
                genotype[index] = '1'
                current_weight += item.get_weight()

        return ''.join(genotype)

    def generate_roulette_population(self):
        total_value = sum(item.get_value() for item in self.items)
        if total_value == 0.0:
            raise ValueError("Суммарная ценность предметов равна 0. Рулетка не может работать.")

        for _ in range(self.size):
            genotype = ['0'] * len(self.items)
            current_weight = 0.0

            while current_weight < self.max_weight:
                roulette_spin = random.uniform(0, total_value)
                cumulative_value = 0.0
                item_added = False

                for j, item in enumerate(self.items):
                    if genotype[j] == '0':
                        cumulative_value += item.get_value()
                        if cumulative_value >= roulette_spin:
                            if current_weight + item.get_weight() <= self.max_weight:
                                genotype[j] = '1'
                                current_weight += item.get_weight()
                                item_added = True
                            break

                if not item_added:
                    break

            genotype_str = ''.join(genotype)
            individual = Individual(genotype_str, self.items, self.max_weight)
            self.individuals.append(individual)

    def get_individuals(self) -> List[Individual]:
        return self.individuals

    def get_size(self) -> int:
        return self.size

    def get_best_individual(self) -> Individual:
        if not self.individuals:
            raise ValueError("Популяция пуста.")
        best = self.individuals[0]
        for individual in self.individuals[1:]:
            if individual.fitness > best.fitness:  # Используем свойство вместо метода
                best = individual
        return best

    def add_individuals(self, new_individuals: List[Individual]):
        self.individuals.extend(new_individuals)

    def replace_with_children(self, children: List[Individual]):
        self.individuals = children.copy()

    def update_population(self, offspring: List[Individual], selection_method: SelectionMethod):
        self.individuals.extend(offspring)
        self.individuals = selection_method.select_parents(self.individuals, self.size)
