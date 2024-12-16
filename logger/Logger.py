from genetic import Individual, Population

class Logger:
    def __init__(self):
        pass

    def log_generation(self, generation: int, population: Population):
        best = population.get_best_individual()
        print()
        if generation != 0:
            log_message = f"Поколение {generation}: Лучшая приспособленность = {best.get_fitness}"
            print(log_message)
            print(f"Лучшая особь: {best}")
        else:
            print("\n")
            print("==========================Начало Алгоритма=======================")

    def log_final(self, population: Population):
        best = population.get_best_individual()
        final_message = f"Алгоритм завершён. Лучшая особь: {best}"
        print(final_message)
