from utils.population_selection import generate_new_population
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

if __name__ == "__main__":
    np.random.seed(42)
    size = int(input("Enter population size: \n"))
    population = list(map(lambda x: np.binary_repr(x, width=7), np.random.randint(low=0, high=64, size=size)))
    int_pop = list(map(lambda x: int(x, 2), population))
    mean_values = [sum(int_pop)/len(int_pop)]    
    print("Starting values:") 
    print(int_pop)
    for i in tqdm(range(20000)):
        population = generate_new_population(population)
        int_pop = list(map(lambda x: int(x, 2), population))
        mean_values.append(sum(int_pop)/len(int_pop))
    print("Terminating values:") 
    print(int_pop)
    plt.plot(mean_values)
    plt.show()