from __future__ import annotations

from abc import abstractmethod

from ...models import Individual

from typing import List, Tuple


class Selector:
    @abstractmethod
    def make_selection(self, population: List[Individual], selection_amount: int = -1) -> List[Tuple[Individual, Individual]]:
        """Make a selection of individuals based on their fitness values

        Arguments:
        poputlation -- individuals from which the selection is made
        selection_amount -- the amount of tuples that are created. -1 defaults to half the population size
        
        Returns:
        list of tuples where each tuple represents a pair of individuals that will reproduce
        """
        pass