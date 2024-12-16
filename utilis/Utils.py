import random
from typing import List
from items import Item

class Utils:
    # Создаём статический экземпляр генератора случайных чисел
    random_instance = random.Random()

    @staticmethod
    def generate_valid_genotype(length: int, items: List['Item'], max_weight: float) -> str:
        """
        Генерирует допустимый генотип длины `length`, где каждый ген представляет наличие (1) или отсутствие (0) элемента.
        Обеспечивает, что общий вес выбранных элементов не превышает `max_weight`.
        """
        genotype = []
        current_weight = 0.0

        for i in range(length):
            add_item = Utils.random_instance.choice([True, False])
            if add_item and current_weight + items[i].get_weight() <= max_weight:
                genotype.append('1')
                current_weight += items[i].get_weight()
            else:
                genotype.append('0')

        return ''.join(genotype)

    @staticmethod
    def calculate_weight(genotype: str, items: List['Item']) -> float:
        """
        Вычисляет общий вес элементов, выбранных в генотипе.
        """
        total_weight = 0.0
        for i, gene in enumerate(genotype):
            if gene == '1':
                total_weight += items[i].get_weight()
        return total_weight

    @staticmethod
    def calculate_value(genotype: str, items: List['Item']) -> float:
        """
        Вычисляет общую ценность элементов, выбранных в генотипе.
        """
        total_value = 0.0
        for i, gene in enumerate(genotype):
            if gene == '1':
                total_value += items[i].get_value()
        return total_value

    @staticmethod
    def get_sorted_indices_by_value_to_weight_ratio(items: List['Item'], genotype: str) -> List[int]:
        """
        Возвращает список индексов выбранных элементов, отсортированных по соотношению ценности к весу.
        """
        # Собираем индексы элементов, где генотип равен '1'
        indices = [i for i, gene in enumerate(genotype) if gene == '1']

        # Сортируем индексы по соотношению value/weight
        sorted_indices = sorted(
            indices,
            key=lambda ix: items[ix].get_value() / items[ix].get_weight() if items[ix].get_weight() != 0 else 0
        )

        return sorted_indices
