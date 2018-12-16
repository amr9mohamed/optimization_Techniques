from helpers import *
import random
import argparse
import genetic_alg as ga
from datetime import datetime

def run(args):
    genes = generate_genes_from_csv(args.cities)

    if args.verbose:
        print("-- Running TSP-GA with {} cities --".format(len(genes)))
        # print(genes)

    best_routes,best_dists = ga.run_alg(genes, args.pop_size, args.n_gen,
                               args.mut_rate, args.verbose)

    # if args.verbose:
    #     print("-- Drawing Route --")

    # utils.plot(history['cost'], history['route'])

    if args.verbose:
        print("-- Done --")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--pop_size', type=int, default=300, help='Population size')
    parser.add_argument('--mut_rate', type=float, default=0.02, help='Mutation rate')
    parser.add_argument('--n_gen', type=int, default=10, help='Number of generations to kick before stopping')
    parser.add_argument('--cities', type=str, default="../cities.csv", help='File containing coordinates of cities')
    parser.add_argument('-v', '--verbose', type=int, default=1)

    # random.seed(datetime.now())
    args = parser.parse_args()

run(args)