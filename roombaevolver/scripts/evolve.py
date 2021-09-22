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
    process_pool: Pool = Pool(processes=7)
    # process_pool: Pool = None

    start = time()

    # start from scratch
    # ga = GeneticAlgorithm(RNNGene, RNNEvaluator(KAMI_V2, (6.5, .75, pi / 2), simulation_time=45), TournamentSelector(20), population_size=150, mutation_probability=.02, process_pool=process_pool, inputs=12, outputs=2, output_dir='results/roombaevolver/')
    
    # start from specific generation
    generation = 49
    population = GeneticAlgorithm.load_state('results/roombaevolver/population-generation-{generation}'.format(generation=generation))
    ga = GeneticAlgorithm(RNNGene, RNNEvaluator(KAMI_V2, (6.5, .75, pi / 2), simulation_time=45), TournamentSelector(20), population_size=150, mutation_probability=.02, population=population, generation=generation, process_pool=process_pool, inputs=12, outputs=2, output_dir='results/roombaevolver/')

    ga.start()

    print("{} seconds have passed.".format(round(time() - start, 2)))