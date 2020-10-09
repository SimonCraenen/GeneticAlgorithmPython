from __future__ import annotations

from typing import Tuple

from abc import abstractmethod, abstractstaticmethod


class Gene:
    @abstractmethod
    def mutate(self, mutation_probability: float):
        """Mutate and adjust this gene"""
        pass

    @abstractmethod
    def crossover(self, other: Gene) -> Tuple[Gene, Gene]:
        """Crossover this gene with the supplied gene to create two child genes

        Arguments:
        other -- other gene used for gene crossover

        Returns:
        tuple of resulting genes
        """
        pass

    @abstractstaticmethod
    def initialise(**kwargs) -> Gene:
        pass
