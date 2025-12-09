from custom_env import XFOILEnv
import pygad
from utils import plot_airfoil
from utils import plot_performance

env = XFOILEnv()

# using genetic algorithm
env.reset()

def fitness_func(ga_instance, solution, solution_idx):
    # Calculate the output based on the solution and function_inputs
    env.step(solution)
    env.reset()
    output = env.performance_log[-1]  # Assuming the last performance metric is what we want
    fitness = output
    return fitness

gene_space = [{'low': -0.15, 'high': 0.15},  
               {'low': -0.15, 'high': 0.15},
               {'low': -0.15, 'high': 0.15},
               {'low': -0.15, 'high': 0.15},
               {'low': -0.15, 'high': 0.15},
               {'low': -0.15, 'high': 0.15},
               {'low': -0.15, 'high': 0.15},
               {'low': -0.15, 'high': 0.15},] 

ga_instance = pygad.GA(num_generations = 64,
                        sol_per_pop = 64,
                        num_parents_mating = 32,
                        parent_selection_type = "tournament",
                        K_tournament = 4,
                        crossover_probability = 0.85,
                        mutation_probability = 0.08,
                        keep_elitism = 2,
                        fitness_func=fitness_func,
                        num_genes=8,
                        gene_space=gene_space)

ga_instance.run()
plot_performance(env)
plot_airfoil(env)