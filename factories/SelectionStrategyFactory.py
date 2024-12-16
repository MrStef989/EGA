from methods.selection import SelectionMethod, TournamentSelection, RouletteWheelSelection, RandomSelection

class SelectionStrategyFactory:
    def __init__(self):
        pass

    @staticmethod
    def create(type: str) -> SelectionMethod:
        if type.lower() == "tournament":
            return TournamentSelection(3)  # Assuming 3 is a parameter for TournamentSelection
        elif type.lower() == "roulettewheel":
            return RouletteWheelSelection()
        elif type.lower() == "random":
            return RandomSelection()
        else:
            raise ValueError(f"Неизвестный тип метода отбора: {type}")
