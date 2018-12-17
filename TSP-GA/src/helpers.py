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
    # plot_route(individual)


    plt.show()

# def plot_route(individual):
#     m = Basemap(projection='lcc', resolution=None,
#                 width=5E6, height=5E6,
#                 lat_0=-15, lon_0=-56)

#     plt.axis('off')
#     plt.title("Shortest Route")

#     for i in range(0, len(individual.genes)):
#         x, y = m(individual.genes[i].lng, individual.genes[i].lat)

#         plt.plot(x, y, 'ok', c='r', markersize=5)
#         if i == len(individual.genes) - 1:
#             x2, y2 = m(individual.genes[0].lng, individual.genes[0].lat)
#         else:
#             x2, y2 = m(individual.genes[i+1].lng, individual.genes[i+1].lat)

#     plt.plot([x, x2], [y, y2], 'k-', c='r')