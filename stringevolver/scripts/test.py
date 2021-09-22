from sys import path as sys_path
from typing import List

sys_path.append("./")

from core.algorithm.selection import Selector, TournamentSelector, RouletteSelector
from core.models import Individual, individual
from core.algorithm import evaluation
from stringevolver.models import StringGene
from stringevolver.evaluation import StringEvaluator

def run_crossover():
    gene_one = StringGene.initialise(gene_length=11)
    gene_two = StringGene.initialise(gene_length=11)

    new_gene_one, new_gene_two = gene_one.crossover(gene_two)

    print(gene_one.string, gene_two.string)
    print('after crossover')
    print(new_gene_one.string, new_gene_two.string)

def run_mutation():
    gene = StringGene.initialise(gene_length=11)
    print('{:>20}  {:>20}'.format('before mutate:', gene.string))
    gene.mutate(mutation_probability=.2)
    print('{:>20}  {:>20}'.format('after mutate:', gene.string))

def run_evaluation():
    evaluator = StringEvaluator(target='hello world')

    individual = Individual(StringGene('hello world'))
    fitness = evaluator.evaluate(individual)

    print('{:>14}  {:>10} '.format('gene', 'fitness'))
    print('{:>14}  {:>10} {:<20}'.format(individual.gene.string, round(fitness, 3), 'should = 1'))

    individual = Individual(StringGene('heddo wordd'))
    fitness = evaluator.evaluate(individual)
    print('{:>14}  {:>10} {:<20}'.format(individual.gene.string, round(fitness, 3), 'should = 8/11'))

def run_selector(selector: Selector):
    population: List[Individual] = [
        Individual(StringGene('hello world'), fitness=1),
        Individual(StringGene('hello papaa'), fitness=.7),
        Individual(StringGene('hello mamaa'), fitness=.7)
    ]

    selected_individual = selector.select_individual(population)

    print('selected individual', selected_individual.gene)

if __name__ == "__main__":
    run_crossover()
    # run_mutation()
    # run_evaluation()
    # run_selector(TournamentSelector(tournament_size=3))
    # run_selector(RouletteSelector())