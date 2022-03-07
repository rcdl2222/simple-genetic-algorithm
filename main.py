from utils.population_selection import generate_new_population
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

if __name__ == "__main__":
    np.random.seed(42)
    size = int(input("Enter population size: \n"))
    population = list(map(np.binary_repr, np.random.randint(low=0, high=64, size=size)))
    int_pop = list(map(lambda x: int(x, 2), population))
    max_values = [max(int_pop)]    
    print(int_pop)
    for i in tqdm(range(10000)):
        population = generate_new_population(population)
        int_pop = list(map(lambda x: int(x, 2), population))
        max_values.append(max(int_pop))
    print(int_pop)
    plt.plot(max_values)
    plt.show()