# Imports
from haversine import haversine
from random import sample,shuffle
from selection import *
from crossover import *
from mutation import *

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

    def get_best_route(self):
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

def sha2lebha_zabatha(popy, selector, mut):
    # use selection technique
    if selector == 'tour':
        new_popy_1 = T_select(popy)
    elif selector == 'rw':
        new_popy_1 = RW_select(popy)

    # use Elitist technique and take top 10% of routes 
    # and replace the others with the new offspring chromosomes
    new_popy_2 = Population(popy.pop_size)

    # create a copy of the previous popy 
    # and remove the top 10% into new popy
    new_popy_1_temp = new_popy_1
    first_10prc = []
    for _ in range(int(popy.pop_size*0.1)):
        curr_best = new_popy_1_temp.get_best_route()
        first_10prc.append(curr_best)
        new_popy_1_temp.possible_routes.remove(curr_best)

    # the crossover process to get new children from old parents 
    # and mutate those children and add them to the rest 
    # of the new population as the 90%
    second_90prc = []
    for _ in range(int(popy.pop_size*0.9)):
        parent1,parent2 = sample(popy.possible_routes,2)
        child = cross_over(parent1,parent2)
        new_child = mutate(child,mut)
        second_90prc.append(child)

    new_popy_2.possible_routes = first_10prc + second_90prc
    shuffle(new_popy_2.possible_routes)
    return new_popy_2

# run genetic algorithm
def run_alg(genes, pop_size, n_gen, mut, selector, verbose):
    
    best_routes = []
    best_dists = []

    popy = Population(pop_size)
    popy.generate_popys(genes)
    
    best_route = popy.get_best_route()
    best_routes.append(best_route)
    best_dists.append(best_route.fitness)
    min_dist = best_route.fitness

    counter = 0

    for _ in range(n_gen):
        new_popy = sha2lebha_zabatha(popy, selector, mut)

        best_route = new_popy.get_best_route()
        best_routes.append(best_route)
        best_dists.append(best_route.fitness)
        curr_dist = best_route.fitness

        if curr_dist < min_dist:
            min_dist = curr_dist
            counter = 0
        else:
            counter+=1

    if verbose:
        print("Best route: ", best_route.genes)
        print("with cost: ", min_dist)

    return best_route,min_dist


