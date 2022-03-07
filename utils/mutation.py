import numpy as np

def mutate_binary(s, p=0.001) -> str:
    """
    Given a binary string, mutate the string with
    probability of p

    Type of mutation: flipping of bits
    
    Parameters:
        s: string to be mutated
        p: probability of mutation
        
    Returns: 
        mutated string
    """
    probability = np.random.uniform(0, 1)
    if probability < p:
        ind = np.random.randint(len(s))
        if s[ind] == "1":
            new_string = s[:ind] + "0" + s[ind+1:]
        else:
            new_string = s[:ind] + "1" + s[ind+1:]
        return new_string 
    return s
