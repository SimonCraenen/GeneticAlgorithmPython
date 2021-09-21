from __future__ import annotations

from abc import abstractmethod

from ...models import Individual

from typing import List, Tuple


class Selector:
    @abstractmethod
    def select_individual(self, population: List[Individual]) -> Individual:
        """Make a selection of individuals based on their fitness values

        Arguments:
        poputlation -- individuals from which the selection is made
        selection_amount -- the amount of tuples that are created. -1 defaults to half the population size
        
        Returns:
        list of tuples where each tuple represents a pair of individuals that will reproduce
        """
        pass

    def make_selection(self, population: List[Individual], selection_amount: int = -1) -> List[Tuple[Individual, Individual]]:
        selection_amount = selection_amount if selection_amount > 0 else int(len(population) / 2)

        selection: List[Tuple[Individual, Individual]] = []


        for i in range(selection_amount):
            winner_one = self.select_individual(population)
            winner_two = self.select_individual(population)

            selection.append((winner_one, winner_two))

        return selection