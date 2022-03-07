import numpy as np

def single_point_crossover(s1, s2, p=0.6):
    """
    Given 2 strings, do a single-point
    crossover

    Parameters:
        s1, s2: strings to be crossed-over
        p: probability of crossover
    
    Returns:
        list of 2 strings
    """
    probability = np.random.uniform(0, 1)
    if probability < p:
        ind = np.random.randint(len(s1))
        new_s1 = s1[:ind] + s2[ind:] 
        new_s2 = s2[:ind] + s1[ind:]
        return [new_s1, new_s2]
    return [s1, s2]
