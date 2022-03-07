import numpy as np
from .fitness import fitness
from .crossover import single_point_crossover
from .mutation import mutate_binary

def roulette_wheel_selection(current, binary=True):
    """
    Do roulette wheel selection on current population
    
    Parameters:
        current: current population
        binary: if strings in population are binary
    
    Returns:
        new population after selection
    """
    size = len(current)
    fitness_array = []
    new_population = []
    for v in current:
        if binary:
            v = int(v, 2)
        fitness_value = fitness(v)
        if fitness_value < 0:
            fitness_array.append(0)
        else:
            fitness_array.append(fitness_value)
    prob_array = [i/sum(fitness_array) for i in fitness_array]
    for i in range(size):
        new_population.append(np.random.choice(current, p=prob_array))
    return new_population

def generate_new_population(current):
    current = roulette_wheel_selection(current)
    new_population = []
    while current != []:
        if len(current) == 1:
            new_population.append(current.pop(0))
        else:
            ind1 = np.random.randint(len(current))
            s1 = current.pop(ind1)
            ind2 = np.random.randint(len(current))
            s2 = current.pop(ind2)
            new_population.extend(single_point_crossover(s1, s2))
    for i in range(len(new_population)):
        new_population[i] = mutate_binary(new_population[i])
    return new_population
