from sys import path as sys_path

sys_path.append("./")

from stringevolver.models import StringGene
from stringevolver.evaluation import StringEvaluator

from core.algorithm import GeneticAlgorithm
from core.algorithm.selection import TournamentSelector, RouletteSelector

from core.models import Individual

from multiprocessing import Pool

from time import time

if __name__ == "__main__":
    process_pool = None

    target = "computer science is pretty cool"

    start = time()
    
    ga = GeneticAlgorithm(StringGene, StringEvaluator(target=target), RouletteSelector(), population_size=10, mutation_probability=.005, process_pool=process_pool, gene_length=len(target), output_dir='results/stringevolver/')
    ga.start()

    print("{} seconds have passed.".format(round(time() - start, 2)))
