from sys import path as sys_path
from math import pi

sys_path.append("./")

from roombaevolver.models.environment import Environment, KAMI_V2
from core.algorithm.selection import Selector, TournamentSelector, RouletteSelector
from core.models import Individual, individual
from core.algorithm import evaluation
from roombaevolver.models import RNNGene
from roombaevolver.evaluation import RNNEvaluator

def run_crossover():
    gene_one = RNNGene.initialise(inputs=12, outputs=2)
    gene_two = RNNGene.initialise(inputs=12, outputs=2)

    new_gene_one, new_gene_two = gene_one.crossover(gene_two)

    print('input weights before crossover')
    print(gene_one.input_weights)
    print()
    print(gene_two.input_weights)
    print()
    print('input weights after crossover')
    print(new_gene_one.input_weights)
    print()
    print(new_gene_two.input_weights)
    print()
    print('recurrent weights before crossover')
    print(gene_one.recurrent_weights)
    print()
    print(gene_two.recurrent_weights)
    print()
    print('recurrent weights after crossover')
    print(new_gene_one.recurrent_weights)
    print()
    print(new_gene_two.recurrent_weights)

def run_mutation():
    gene = RNNGene.initialise(inputs=12, outputs=2)
    print('before mutation')
    print(gene.input_weights)
    print()
    print(gene.recurrent_weights)
    print()
    gene.mutate(mutation_probability=.2)
    print('after mutation')
    print(gene.input_weights)
    print()
    print(gene.recurrent_weights)

def run_evaluation():
    evaluator = RNNEvaluator(KAMI_V2, (6.5, .75, pi / 2), simulation_time=10)

    individual = Individual(RNNGene.initialise(inputs=12, outputs=2))
    fitness = evaluator.evaluate(individual)

    print('fitness', fitness)


if __name__ == "__main__":
    # run_crossover()
    # run_mutation()
    run_evaluation()