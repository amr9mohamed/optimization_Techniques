import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import genetic_alg as ga
from random import sample

def generate_genes_from_csv(filename):
    dataframe = pd.read_csv(filename)
    genes = [ga.Gene(row['city'], row['latitude'], row['longitude']) for _, row in dataframe.iterrows()]
    return genes

def plot(route):
    fig, ax = plt.subplots()
    for i in range(route.n_genes):
        x,y = -route.genes[i].lat,-route.genes[i].lngt
        ax.scatter(x,y)
        ax.annotate(route.genes[i].name, (x, y))

        if i+1 != route.n_genes:
            x_,y_ = -route.genes[i+1].lat,-route.genes[i+1].lngt
        else:
            x_,y_ = -route.genes[0].lat,-route.genes[0].lngt

        plt.plot([x, x_], [y, y_], 'k-', c=(0.5,0.7,0.6))
    plt.show()
