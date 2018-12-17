import pandas as pd
import matplotlib.pyplot as plt
import genetic_alg as ga
from random import sample

def generate_genes_from_csv(filename):
    dataframe = pd.read_csv(filename)
    genes = [ga.Gene(row['city'], row['latitude'], row['longitude']) for _, row in dataframe.iterrows()]

    return genes

def plot(costs, individual, save_to=None):
    plt.figure(1)
    plt.subplot(111)
    pass
    plt.show()
