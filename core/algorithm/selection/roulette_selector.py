from .selector import Selector

from random import choices as rand_choices

from ...models import Individual

from typing import List, Tuple, Dict

from random import uniform


class RouletteSelector(Selector):
    def __init__(self):
        super().__init__()

    def select_individual(self, population: List[Individual]) -> Individual:
        # Look at roulette wheel selection in the slides for inspiration.
        pass