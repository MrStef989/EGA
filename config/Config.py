class Config:
    def __init__(self):
        self.constraint_method = "GenotypeModifier"
        self.population_size = 10
        self.mutation_rate = 0.05
        self.crossover_rate = 0.7
        self.selection_method_type = "Tournament"
        self.crossover_method_type = "OnePoint"
        self.mutation_method_type = "BitFlip"
        self.max_weight = 118
        self.min_diversity = 0.01
        self.max_generations_limit = 500
        self.initial_population_strategy = "Random"
        self.target_fitness = -1.0
        self.max_generations_without_target = -1
        self.use_mu_plus_lambda = True

    def is_use_mu_plus_lambda(self):
        return self.use_mu_plus_lambda

    def set_use_mu_plus_lambda(self, use_mu_plus_lambda):
        self.use_mu_plus_lambda = use_mu_plus_lambda

    def get_target_fitness(self):
        return self.target_fitness

    def set_target_fitness(self, target_fitness):
        self.target_fitness = target_fitness

    def get_max_generations_without_target(self):
        return self.max_generations_without_target

    def set_max_generations_without_target(self, max_generations_without_target):
        self.max_generations_without_target = max_generations_without_target

    def get_initial_population_strategy(self):
        return self.initial_population_strategy

    def set_initial_population_strategy(self, initial_population_strategy):
        self.initial_population_strategy = initial_population_strategy

    def get_constraint_method(self):
        return self.constraint_method

    def set_constraint_method(self, constraint_method):
        self.constraint_method = constraint_method

    def get_population_size(self):
        return self.population_size

    def set_population_size(self, population_size):
        self.population_size = population_size

    def get_mutation_rate(self):
        return self.mutation_rate

    def set_mutation_rate(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def get_crossover_rate(self):
        return self.crossover_rate

    def set_crossover_rate(self, crossover_rate):
        self.crossover_rate = crossover_rate

    def get_selection_method_type(self):
        return self.selection_method_type

    def set_selection_method_type(self, selection_method_type):
        self.selection_method_type = selection_method_type

    def get_crossover_method_type(self):
        return self.crossover_method_type

    def set_crossover_method_type(self, crossover_method_type):
        self.crossover_method_type = crossover_method_type

    def get_mutation_method_type(self):
        return self.mutation_method_type

    def set_mutation_method_type(self, mutation_method_type):
        self.mutation_method_type = mutation_method_type

    def get_max_weight(self):
        return self.max_weight

    def get_min_diversity(self):
        return self.min_diversity

    def set_min_diversity(self, min_diversity):
        self.min_diversity = min_diversity

    def get_max_generations_limit(self):
        return self.max_generations_limit

    def set_max_generations_limit(self, max_generations_limit):
        self.max_generations_limit = max_generations_limit
