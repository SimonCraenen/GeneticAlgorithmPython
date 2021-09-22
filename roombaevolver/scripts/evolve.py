from sys import path as sys_path

sys_path.append("./")

from core.algorithm import GeneticAlgorithm
from core.algorithm.selection import TournamentSelector

from roombaevolver.models import RNNGene, Environment, KAMI_V2
from roombaevolver.evaluation import RNNEvaluator

from multiprocessing import Pool

from time import time

from math import pi

if __name__ == "__main__":
    process_pool: Pool = Pool(processes=11)
    # process_pool: Pool = None

    start = time()

    ga = GeneticAlgorithm(RNNGene, RNNEvaluator(KAMI_V2, (6.5, .75, pi / 2), simulation_time=60), TournamentSelector(20), population_size=250, mutation_probability=.02, process_pool=process_pool, inputs=12, outputs=2, output_dir='results/roombaevolver/')
    ga.start()

    print("{} seconds have passed.".format(round(time() - start, 2)))