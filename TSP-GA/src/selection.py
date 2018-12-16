import genetic_alg as ga
from random import sample

# Tournament Selection
def T_select(popy,pop_size):
    new_popy = ga.Population(pop_size)
    for _ in range(pop_size):
        champs = sample(popy.possible_routes,2)
        if champs[0].fitness < champs[1].fitness:
            new_popy.possible_routes.append(champs[0])
        else:
            new_popy.possible_routes.append(champs[1])
    return new_popy
 