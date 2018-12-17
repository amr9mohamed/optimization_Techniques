import genetic_alg as ga
from random import sample,uniform

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
    new_chromosomes = []
    summation = sum(popa.get_fitness() for popa in popy.possible_routes)
    for _ in range(popy.pop_size):
        pick = uniform(0, summation)
        current = 0
        for chromosome in popy.possible_routes:
            current += chromosome.get_fitness()
            if current > pick:
                new_chromosomes.append(chromosome)
                continue
    new_popy.possible_routes = new_chromosomes
    return new_popy
    

