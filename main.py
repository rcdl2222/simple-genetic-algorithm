from utils.population_selection import generate_new_population
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

if __name__ == "__main__":
    np.random.seed(42)
    size = int(input("Enter population size: \n"))
    crossover = int(input("Enter 1 for single-point crossover; 2 for double-point: \n"))
    epochs = int(input("Enter number of epochs (1 epoch = 1000 iterations): \n"))
    population = list(map(lambda x: np.binary_repr(x, width=7), np.random.randint(low=0, high=64, size=size)))
    int_pop = list(map(lambda x: int(x, 2), population))
    print("Starting values:") 
    print(int_pop)
    epoch_values = []
    for epoch in tqdm(range(epochs)):
        epoch_mean = 0
        for i in range(1000):
            population = generate_new_population(population, crossover=crossover)
            int_pop = list(map(lambda x: int(x, 2), population))
            epoch_mean += (sum(int_pop)/len(int_pop))
        epoch_values.append(epoch_mean / 1000)
    print("Terminating values:") 
    print(int_pop)
    plt.plot(epoch_values)
    plt.show()