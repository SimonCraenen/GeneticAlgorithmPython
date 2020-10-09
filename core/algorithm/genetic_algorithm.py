from __future__ import annotations

from .selection import Selector
from .evaluation import Evaluator
from ..models import Gene, Individual

from abc import abstractmethod

from typing import List, Tuple, Type

from time import time

from pickle import load as pickle_load
from pickle import dump as pickle_dump

from os.path import join as path_join
from os.path import exists as path_exists
from os import makedirs as make_paths


class GeneticAlgorithm:
    def __init__(self, gene_type: Type[Gene], evaluator: Evaluator, selector: Selector, population_size: int, mutation_probability: float, elitism_percentage: float=.05, population: List[Individual] = None, process_pool = None, **kwargs):
        self.process_pool = process_pool

        self.gene_type: Type[Gene] = gene_type
        self.evaluator: Evaluator = evaluator
        self.selector: Selector = selector

        self.mutation_probability: float = mutation_probability
        self.elitism_percentage: float = elitism_percentage
        self.population_size: int = population_size
        
        self.population: List[Individual] = population

        if self.population is None:
            self.population = [Individual.initialise(self.gene_type, **kwargs) for _ in range(self.population_size)]

        self.generation = 1

        self.output_dir = "results/"
        if not path_exists(self.output_dir):
            make_paths(self.output_dir)

    def start(self):
        """Start/Continue the Genetic Algorithm"""

        print("generation {}".format(self.generation), self.population[0].gene, self.population[0].fitness)

        generation_start_time: float = time()

        for _ in range(1000):
            best_individual = self.__iterate()

            generation_end_time = time()
            pickle_dump(best_individual, open(path_join(self.output_dir, "best-generation-{}.p".format(self.generation)), "wb"))
            self.generation += 1
            print("generation {}, {}ms".format(self.generation, round(generation_end_time - generation_start_time, 3) * 1000), best_individual.gene, best_individual.fitness)
            generation_start_time = generation_end_time
            
            if 0.99 < best_individual.fitness:
                break 

    def __iterate(self) -> Individual:
        """A single generation evaluation and reproduction"""

        self.evaluator.evaluate_population(self.population, self.process_pool)
        
        self.population.sort(key=lambda individual: individual.fitness, reverse=True)

        best_individual = self.population[0]

        new_population = self.population[:int(self.population_size * self.elitism_percentage)]

        selected_pairs = self.selector.make_selection(self.population, int((self.population_size - len(new_population)) / 2))

        new_population.extend(self.__do_reproduction(selected_pairs))

        self.population = new_population

        return best_individual

    # @abstractmethod
    def __do_reproduction(self, selected_pairs: List[Tuple[Individual, Individual]]) -> List[Individual]:
        new_population: List[Individual] = []

        for i1, i2 in selected_pairs:
            child_one, child_two = i1.crossover(i2)
            
            child_one.mutate(self.mutation_probability)
            child_two.mutate(self.mutation_probability)

            new_population.append(child_one)
            new_population.append(child_two)

        return new_population

    def save_state(self, path: str):
        """Save a Genetic Algorithm state to file

        Arguments:
        path -- path to the state file (pkl)
        """
        # pickle_dump(self.population, open(path_join(self.output_dir, "population-generation-{}".format(self.generation)), "wb"))
        pass


    @staticmethod
    def load_state(self, path: str) -> GeneticAlgorithm:
        """Load a Genetic Algorithm state from file

        Arguments:
        path -- path to the state file (pkl)
        """
        # self.population = pickle_dump(self.population, open(path_join(self.output_dir, "population-generation-{}".format(self.generation)), "wb"))
        pass