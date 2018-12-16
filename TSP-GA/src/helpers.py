import pandas as pd
import genetic_alg as ga
from random import sample

def generate_genes_from_csv(filename):
    dataframe = pd.read_csv(filename)
    genes = [ga.Gene(row['city'], row['latitude'], row['longitude']) for _, row in dataframe.iterrows()]

    return genes