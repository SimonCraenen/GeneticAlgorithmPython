from .selector import Selector

from random import choices as rand_choices

from ...models import Individual

from typing import List, Tuple


class TournamentSelector(Selector):
    def __init__(self, tournament_size: int = 10):
        super().__init__()
        
        self.tournament_size: int = tournament_size
        
    def select_individual(self, population: List[Individual]) -> Individual:
        # Look at Tournament selection in the slides for inspiration.    
        pass
        