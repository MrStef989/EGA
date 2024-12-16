from config import Config
from genetic import Population

class TerminationCondition:
    def __init__(self, config: Config):
        self.config = config

    def is_met(self, generation: int, population: Population) -> bool:
        if self.config.get_max_generations_limit() > 0 and generation >= self.config.get_max_generations_limit():
            print(f"\nУсловие остановки: Достигнуто максимальное количество поколений ({self.config.get_max_generations_limit()}).\n")
            return True
        else:
            if self.config.get_min_diversity() > 0.0:
                diversity = self.calculate_diversity(population)
                if diversity < self.config.get_min_diversity():
                    print(f"\nУсловие остановки: Разнообразие популяции ниже порога ({diversity} < {self.config.get_min_diversity()}).\n")
                    return True

            if self.config.get_target_fitness() > 0.0:
                best_fitness = population.get_best_individual().get_fitness
                if best_fitness >= self.config.get_target_fitness():
                    print(f"\nУсловие остановки: Достигнута целевая приспособленность ({best_fitness} >= {self.config.get_target_fitness()}).\n")
                    return True

            if self.config.get_target_fitness() > 0.0 and generation >= self.config.get_max_generations_without_target():
                print(f"\nУсловие остановки: Целевая приспособленность не достигнута за {self.config.get_max_generations_without_target()} поколений.\n")
                return True
            else:
                return False

    def calculate_diversity(self, population: Population) -> float:
        unique_genotypes = set()
        for individual in population.get_individuals():
            unique_genotypes.add(individual.get_genotype)
        return len(unique_genotypes) / float(population.get_size())
