import genetic_alg as ga
from random import sample

# Tournament Selection
def T_select(popy):
    new_popy = ga.Population(popy.pop_size)
    for _ in range(popy.pop_size):
        champs = sample(popy.possible_routes,2)
        if champs[0].fitness < champs[1].fitness:
            new_popy.possible_routes.append(champs[0])
        else:
            new_popy.possible_routes.append(champs[1])
    return new_popy

# Roulette-Wheel Selection
def RW_select(popy):
    new_popy = ga.Population(popy.pop_size)
    rand_n = []
    summation = sum(popa.get_fitness() for popa in popy.possible_routes)
    

