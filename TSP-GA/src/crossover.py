import genetic_alg as ga
from random import sample,randint

def cross_over(parent1,parent2):
    pivot = randint(0, parent1.n_genes - 1)

    genes_1, genes_2 = parent1,parent2

    genes_1[0:pivot] = parent1.genes[0:pivot]
    [genes_2.remove(i) for i in genes_1[0:pivot]]
    genes_1[pivot:] = genes_2
    child1 = ga.Chromosome(genes_1)

    genes_1, genes_2 = parent1,parent2

    genes_2[0:pivot] = parent2.genes[0:pivot]
    [genes_1.remove(i) for i in genes_2[0:pivot]]
    genes_2[pivot:] = genes_1
    child2 = ga.Chromosome(genes_2)
    
    return child1,child2
