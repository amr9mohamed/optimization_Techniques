import numpy as np
import random
import matplotlib.pyplot as plt

def func(X):
    return 1 / (1 + X[0]**2 + X[1]**2)

def acceptance_probability(old, new, T):
    return np.exp(-np.sum(new - old) / T)

def anneal(sol):
    old_cost = func(sol)
    T0 = 1.0
    T_min = 0.00001
    alpha = 0.9
    Ti = T0
    best_sol = sol
    best_cost = old_cost
    while Ti > T_min:
        for _ in range(100):
            new_sol = sol *(1 - Ti/T0 ) + (Ti/T0) * random.uniform(-5, 5)
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

        Ti = Ti*alpha

    return best_sol, best_cost

X = np.array([(-1), (-1)])
sol, cost = anneal(X)
print(sol, cost)

