from methods.crossover import CrossoverMethod, OnePointCrossover, TwoPointCrossover, UniformCrossover

class CrossoverStrategyFactory:
    def __init__(self):
        pass

    @staticmethod
    def create(type: str) -> CrossoverMethod:
        if type.lower() == "onepoint":
            return OnePointCrossover()
        elif type.lower() == "twopoint":
            return TwoPointCrossover()
        elif type.lower() == "uniform":
            return UniformCrossover()
        else:
            raise ValueError(f"Неизвестный тип метода кроссовера: {type}")
