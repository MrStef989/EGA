import random
from typing import List
from genetic.Individual import Individual
from genetic import Population
from config.Config import Config
from evalutor.FitnessEvalutor import FitnessEvalutor
from factories import ConstraintHandlerFactory, CrossoverStrategyFactory, MutationStrategyFactory, SelectionStrategyFactory
from methods.crossover import CrossoverMethod
from methods.handler import ConstraintStrategy
from methods.mutation import MutationMethod
from methods.selection import SelectionMethod
from logger import Logger
from termination import TerminationCondition
from items.Item import Item

class GeneticAlgorithm:
    def __init__(self, config: Config, items: List[Item], population: Population):
        self.config = config
        self.items = items
        self.population = population
        self.selection_method = SelectionStrategyFactory.create(config.get_selection_method_type())
        self.crossover_method = CrossoverStrategyFactory.create(config.get_crossover_method_type())
        self.mutation_method = MutationStrategyFactory.create(config.get_mutation_method_type(), config.get_mutation_rate())
        self.fitness_evaluator = FitnessEvalutor()
        self.constraint_handler = ConstraintHandlerFactory.create(config.get_constraint_method(), config.get_max_weight())
        self.logger = Logger()
        self.termination_condition = TerminationCondition(config)

    def run(self):
        self.fitness_evaluator.evaluate(self.population.get_individuals(), self.items, self.config.get_max_weight())
        self.logger.log_generation(0, self.population)

        generation = 1
        while not self.termination_condition.is_met(generation, self.population):
            print(f"\n=== Поколение {generation} ===")
            print("Популяция перед воспроизводством:")

            for individual in self.population.get_individuals():
                print(individual)

            parents = self.selection_method.select_parents(self.population.get_individuals(), self.config.get_population_size())
            print("\nРодители, отобранные для кроссовера:")

            for parent in parents:
                print(parent)

            children = []
            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[i + 1] if i + 1 < len(parents) else parents[0]
                if random.random() >= self.config.get_crossover_rate():
                    children.append(Individual(parent1.get_genotype, self.items, self.config.get_max_weight()))
                    children.append(Individual(parent2.get_genotype, self.items, self.config.get_max_weight()))
                    children.append(Individual(parent1.get_genotype, self.items, self.config.get_max_weight()))
                else:
                    offspring = self.crossover_method.crossover([parent1, parent2])

                    while len(offspring) < 3:
                        offspring.append(Individual(parent1.get_genotype, self.items, self.config.get_max_weight()))

                    children.extend(offspring[:3])

            print("\nПотомки после кроссовера (до мутации):")
            for child in children:
                print(child)

            for child in children:
                self.mutation_method.mutate(child)

            print("\n--------------------------Прошла мутация-------------------------\n")
            print("============Обработка ошибок(если есть дефектные особи)===========")

            for child in children:
                self.constraint_handler.enforce_constraints(child, self.items)

            print("\n============Обработка ошибок(если есть дефектные особи)===========\n")
            print("\nПотомки после мутации:")

            for child in children:
                print(child)

            if self.config.is_use_mu_plus_lambda():
                self.population.add_individuals(children)
                print("\nПопуляция после добавления потомков (до отбора, метод μ + λ):")

                for individual in self.population.get_individuals():
                    print(individual)

                self.population.update_population(children, self.selection_method)
            else:
                self.population.replace_with_children(children)
                print("\nПопуляция после замены родителей потомками (до отбора, метод μ, λ):")

                for individual in self.population.get_individuals():
                    print(individual)

                self.population.update_population(children, self.selection_method)

            self.logger.log_generation(generation, self.population)
            generation += 1

        self.logger.log_final(self.population)
