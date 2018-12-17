import numpy as np
import random
import matplotlib.pyplot as plt

def func(X):
    return 1 / (1 + X[0]**2 + X[1]**2)

def acceptance_probability(old_cost, new_cost, t):
    return np.exp(-np.sum(new_cost - old_cost) / t)

def neighbor(sol, T0, Ti, lower, upper):
    return sol *(1 - Ti/T0 ) + (Ti/T0) * random.uniform(lower, upper)

def anneal(sol, lower, upper):
    old_cost = func(sol)
    T0 = 1.0
    T_min = 0.00001
    alpha = 0.9
    Ti = T0
    best_sol = sol
    best_cost = old_cost
    
    while Ti > T_min:
        for _ in range(100):
            new_sol = neighbor(sol, T0, Ti, lower, upper)
            new_cost = func(new_sol)
            if new_cost > old_cost:
                sol = new_sol
                old_cost = new_cost
                best_sol = new_sol if new_cost > best_cost else best_sol
                best_cost = func(best_sol)
            else:
                ap = acceptance_probability(old_cost, new_cost, Ti)
                if ap > np.random.random():
                    sol = new_sol
                    old_cost = new_cost
        
        Ti = alpha*Ti
            
    return best_sol, best_cost

lower = -100
upper =  100
X = np.random.randint(low=lower, high=upper, size=(2))
sol, cost = anneal(X, lower=lower, upper=upper)
print(f'Best solution is {sol}, function at this point is {cost}')
