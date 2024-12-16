from methods.handler import ConstraintStrategy, GenotypeModifier, ExcludeHandler

class ConstraintHandlerFactory:
    def __init__(self):
        pass

    @staticmethod
    def create(method: str, max_weight: float) -> ConstraintStrategy:
        if method.lower() == "genotypemodifier":
            return GenotypeModifier(max_weight)
        elif method.lower() == "exclude":
            return ExcludeHandler(max_weight)
        else:
            raise ValueError(f"Неизвестный метод обработки ограничений: {method}")
