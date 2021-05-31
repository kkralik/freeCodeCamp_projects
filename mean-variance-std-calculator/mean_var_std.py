
import numpy as np

def calculate(list):
    # make sure the list is long enough
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}
    a = np.array(list).reshape(3,3)
    
    # means:
    means_a0 = a.mean(axis = 0).tolist()
    means_a1 = a.mean(axis = 1).tolist()
    calculations['mean'] = [means_a0, means_a1, a.mean()]
    
    # variance:
    variance_a0 = a.var(axis = 0).tolist()
    variance_a1 = a.var(axis = 1).tolist()
    calculations['variance'] = [variance_a0, variance_a1, a.var()]
    
    # standard deviation, max, min, sum
    calculations['standard deviation'] = [a.std(axis = 0).tolist(), a.std(axis = 1).tolist(), a.std()]
    calculations['max'] = [a.max(axis = 0).tolist(), a.max(axis = 1).tolist(), a.max()]
    calculations['min'] = [a.min(axis = 0).tolist(), a.min(axis = 1).tolist(), a.min()]
    calculations['sum'] = [a.sum(axis = 0).tolist(), a.sum(axis = 1).tolist(), a.sum()]

    return calculations
