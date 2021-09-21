from abc import abstractmethod

from ...models import Individual

from typing import List

from multiprocessing import Pool

class Evaluator:
    @abstractmethod
    def evaluate(self, individual: Individual) -> float:
        """Evaluate an individual

        Arguments:
        individual -- individual to be evaluated

        Returns:
        int -- resulting evaluation score
        """        
        pass

    def evaluate_population(self, population: List[Individual], process_pool: Pool = None):
        if process_pool:
            results = []
            for individual in population:
                results.append(process_pool.apply_async(self.evaluate, args=(individual,)))

            for index, result in enumerate(results):
                population[index].fitness = result.get()

        else:
            for individual in population:
                individual.fitness = self.evaluate(individual)
