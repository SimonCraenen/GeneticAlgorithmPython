from .selector import Selector

from random import choices, choice, sample

from ...models import Individual

from typing import List



class RouletteSelector(Selector):
    def __init__(self):
        super().__init__()

    def select_individual(self, population: List[Individual]) -> Individual:
        # Look at roulette wheel selection in the slides for inspiration.
        pass