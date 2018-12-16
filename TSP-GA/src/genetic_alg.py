# Imports
from haversine import haversine
from random import sample
from selection import *

# Gene: a gene for every city in our csv file
class Gene:
    # a dict for all distances between all cities
    distances = {}

    def __init__(self, name, lat, lngt):
        self.name = name
        self.lat = lat
        self.lngt = lngt
        
    def get_distance(self, dst):
        p1 = self.name + '_' + dst.name
        p2 = dst.name + '_' + self.name

        if p1 in Gene.distances:
            return Gene.distances[p1]
        if p2 in Gene.distances:
            return Gene.distances[p2]
        
        src = (self.lat, self.lngt)
        dest = (dst.lat, dst.lngt)

        Gene.distances[p1] = haversine(src,dest)
        return Gene.distances[p1]

    def __repr__(self):
        return str(self.name)

# Population: a population class containing all possible routes
class Population:
    def __init__(self, pop_size):
        self.pop_size = pop_size
        self.possible_routes = []

    def generate_popys(self, genes):
        for _ in range(self.pop_size):
            self.possible_routes.append(Chromosome(sample(genes, len(genes))))

    def get_best(self):
        besto = self.possible_routes[0]
        for pr in self.possible_routes[1:]:
            if pr.get_fitness() < besto.get_fitness():
                besto = pr
        return besto
    
    def verbosa_bosa(self):
        for i in range(self.pop_size):
            print(self.possible_routes[i].genes)
        
# Chromosome: a class for a possible route containing genes(cities)
class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.n_genes = len(genes)
        self.fitness = 0

    def get_fitness(self):
        if self.fitness != 0:
            return self.fitness

        for i in range(self.n_genes):
            if i+1 == self.n_genes:
                self.fitness += self.genes[i].get_distance(self.genes[0])
            else:    
                self.fitness += self.genes[i].get_distance(self.genes[i+1])
        return self.fitness

# run genetic algorithm
def run_alg(genes, pop_size, n_gen, mut, verbose):
    
    best_routes = []
    best_dists = []

    popy = Population(pop_size)
    popy.generate_popys(genes)

    # if verbose:
    #     popy.verbosa_bosa()
    
    best_route = popy.get_best()
    best_routes.append(best_route)
    best_dists.append(best_route.fitness)
    min_dist = best_route.fitness

    for _ in range(n_gen):
        # select_recombine()

        new_popy = T_select(popy,pop_size)
        best_routes.append(best_route)
        best_dists.append(best_route.fitness)
        curr_dist = new_popy.get_best().get_fitness()

        if curr_dist < min_dist:
            min_dist = curr_dist
            print("changed")
        # else:
        #     print("no better route")

    if verbose:
        print("Best route: ", best_route.genes)
        print("with cost: ", min_dist)

    return best_routes,best_dists


