# Example in MutationStrategyFactory.py
from methods.mutation.MutationMethod import MutationMethod
from methods.mutation.BitFlipMutation import BitFlipMutation
from methods.mutation.InversionMutation import InversionMutation
from methods.mutation.SwapMutation import SwapMutation


class MutationStrategyFactory:
    def __init__(self):
        pass

    @staticmethod
    def create(type: str, mutation_rate: float) -> MutationMethod:
        if type.lower() == "bitflip":
            return BitFlipMutation(mutation_rate)
        elif type.lower() == "inversion":
            return InversionMutation(mutation_rate)
        elif type.lower() == "swap":
            return SwapMutation(mutation_rate)
        else:
            raise ValueError(f"Неизвестный тип метода мутации: {type}")
