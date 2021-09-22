from .selector import Selector

from random import choices

from ...models import Individual

from typing import List


class RouletteSelector(Selector):
    def __init__(self):
        super().__init__()

    def select_individual(self, population: List[Individual]) -> Individual:
        return choices(population=population, weights=[individual.fitness for individual in population])[0]