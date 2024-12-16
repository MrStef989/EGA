import sys
from genetic.Population import Population
from genetic.GeneticAlgorithm import GeneticAlgorithm
from config.Config import Config
from items.ItemReader import ItemReader


def main():
    config = Config()
    file_path = "item"

    try:
        items = ItemReader.read_items(file_path)
    except IOError as e:
        print(f"Ошибка чтения файла: {e}", file=sys.stderr)
        return

    if not items:
        print("Список предметов пуст. Проверьте содержимое файла.", file=sys.stderr)
        return

    population_size = int(input("Введите количество особей в популяции: "))
    config.set_population_size(population_size)

    print("Выберите метод формирования начальной популяции:")
    print("1. Случайный")
    print("2. Гибридный (жадный с элементами рандома)")
    print("3. Рулетка (ценность определяет шанс)")
    population_choice = int(input())

    if population_choice == 2:
        config.set_initial_population_strategy("Hybrid")
    elif population_choice == 3:
        config.set_initial_population_strategy("Roulette")
    else:
        config.set_initial_population_strategy("Random")

    config.set_mutation_rate(float(input("Введите вероятность мутации (например, 0.05 для 5%): ")))
    config.set_crossover_rate(float(input("Введите вероятность кроссовера (например, 0.7 для 70%): ")))

    print("Выберите метод кроссовера:")
    print("1 - Одноточечный кроссовер")
    print("2 - Двухточечный кроссовер")
    print("3 - Универсальный кроссовер")
    crossover_choice = input()

    if crossover_choice == "1":
        config.set_crossover_method_type("OnePoint")
    elif crossover_choice == "2":
        config.set_crossover_method_type("TwoPoint")
    elif crossover_choice == "3":
        config.set_crossover_method_type("Uniform")
    else:
        print("Некорректный выбор. Используется метод по умолчанию: Одноточечный кроссовер.")
        config.set_crossover_method_type("OnePoint")

    print("Введите метод отбора/формирования пар (1 - Турнирный, 2 - Рулеточный, 3 - Случайный): ")
    selection_choice = input()

    if selection_choice == "1":
        config.set_selection_method_type("Tournament")
    elif selection_choice == "2":
        config.set_selection_method_type("RouletteWheel")
    elif selection_choice == "3":
        config.set_selection_method_type("Random")
    else:
        print("Некорректный выбор. Используется метод по умолчанию: Турнирный.")
        config.set_selection_method_type("Tournament")

    print("Выберите тип мутации:")
    print("1 - Битовая мутация")
    print("2 - Инверсная мутация")
    print("3 - Свап-мутация ")
    mutation_choice = input()

    if mutation_choice == "1":
        config.set_mutation_method_type("BitFlip")
    elif mutation_choice == "2":
        config.set_mutation_method_type("Inversion")
    elif mutation_choice == "3":
        config.set_mutation_method_type("Swap")
    else:
        print("Некорректный выбор. Используется метод по умолчанию: Битовая мутация.")
        config.set_mutation_method_type("BitFlip")

    print("Выберите метод обработки ограничений (1 - Смена генотипа, 2 - Исключение): ")
    constraint_choice = input()

    if constraint_choice == "1":
        config.set_constraint_method("GenotypeModifier")
    elif constraint_choice == "2":
        config.set_constraint_method("Exclude")
    else:
        print("Некорректный выбор. Используется метод по умолчанию: Смена генотипа.")
        config.set_constraint_method("GenotypeModifier")

    print("Выберите метод формирования нового поколения:")
    print("1. μ + λ (родители и потомки участвуют в следующем поколении)")
    print("2. μ, λ (только потомки участвуют в следующем поколении)")
    generation_method_choice = int(input())
    config.set_use_mu_plus_lambda(generation_method_choice == 1)

    print("Выберите условие остановки:")
    print("1. Остановиться по максимальному количеству поколений.")
    print("2. Остановиться по минимальному разнообразию популяции.")
    print("3. Остановиться при достижении заданной приспособленности или лимита поколений.")
    stop_condition_choice = int(input("Введите ваш выбор (1, 2 или 3): "))

    if stop_condition_choice == 1:
        max_generations = int(input("Введите максимальное количество поколений: "))
        config.set_max_generations_limit(max_generations)
        config.set_min_diversity(-1.0)
    elif stop_condition_choice == 2:
        min_diversity = float(
            input("Введите минимальное разнообразие популяции (например, 0.1 для 10%): ").replace(",", "."))
        config.set_min_diversity(min_diversity)
        config.set_max_generations_limit(-1)
    elif stop_condition_choice == 3:
        target_fitness = float(input("Введите целевую приспособленность: "))
        max_generations_without_target = int(input("Введите максимальное количество поколений для поиска цели: "))
        config.set_target_fitness(target_fitness)
        config.set_max_generations_without_target(max_generations_without_target)
    else:
        print("Некорректный выбор. Используется дефолтное условие: максимальное количество поколений.")
        config.set_max_generations_limit(500)
        config.set_min_diversity(-1.0)

    population = Population(config, items)
    genetic_algorithm = GeneticAlgorithm(config, items, population)
    genetic_algorithm.run()

    best_individual = population.get_best_individual()
    print(f"\033[0;33mЛучшая особь: {best_individual}")
    print("Алгоритм завершён.\033[0m")


if __name__ == "__main__":
    main()
