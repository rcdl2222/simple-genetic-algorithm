import numpy as np

def fitness(x):
    """Define simple fitness function as
    x^^2"""
    return (-(x-30)**2) + 100