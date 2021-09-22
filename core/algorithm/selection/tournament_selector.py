from .selector import Selector

from ...models import Individual

from random import sample

from typing import List


class TournamentSelector(Selector):
    def __init__(self, tournament_size: int = 10):
        super().__init__()
        
        self.tournament_size: int = tournament_size
        
    def select_individual(self, population: List[Individual]) -> Individual:
        tournament = sample(population=population, k=self.tournament_size)
        return max(tournament, key=lambda individual: individual.fitness)
        