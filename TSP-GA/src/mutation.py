import genetic_alg as ga
from random import sample,random

# mutate the chromosome with mut rate
def mutate(chromosome,mut):
    for _ in range(chromosome.n_genes):
        if random() < mut:
            geno1,geno2 = sample(chromosome.genes,2)
            chromsome = swap(chromosome,geno1,geno2)

# swap genes as a mutation
def swap(chromosome,geno1,geno2):
    p1,p2 = chromosome.genes.index(geno1),chromosome.genes.index(geno2)
    chromosome.genes[p1],chromosome.genes[p2] = chromosome.genes[p2],chromosome.genes[p1]
    return chromosome