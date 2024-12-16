from typing import List
from items.Item import Item  # Предполагается, что класс Item уже определен
from utilis.Utils import Utils

# genetic/Individual.py
class Individual:
    def __init__(self, genotype: str, items: List[Item], max_weight: float):
        self.genotype = genotype
        self.items = items
        self.max_weight = max_weight
        self.calculate_characteristics(items, max_weight)

    def calculate_characteristics(self, items: List[Item], max_weight: float):
        self.weight = Utils.calculate_weight(self.genotype, items)
        self.fitness = Utils.calculate_value(self.genotype, items)

    @property
    def get_genotype(self) -> str:
        return self.genotype

    @property
    def get_weight(self) -> float:
        return self.weight

    @property
    def get_fitness(self) -> float:
        return self.fitness

    @property
    def get_items(self) -> List[Item]:
        return self.items

    @property
    def get_max_weight(self) -> float:
        return self.max_weight

    def __str__(self) -> str:
        return f"Генотип: {self.genotype} | Вес: {self.weight:.2f} | Приспособленность: {self.fitness:.2f}"
