from __future__ import annotations

from core.models import Gene

from typing import Tuple

from numpy.random import randint, uniform
from random import choices as rand_choices


alphabet = 'abcdefghijklmnopqrstuvwxyz -'

class StringGene(Gene):
    def __init__(self, string: str):
        self.string = string

    def mutate(self, mutation_probability: float):
	    # implement this
        # should adjust [self.string]
        pass
        
    def crossover(self, other: StringGene) -> Tuple[StringGene, StringGene]:
       	# implement this (return two string genes with the appropriate values)
        return self, other

    def __repr__(self):
        return '[Gene - {string}]'.format(string=self.string)

    @staticmethod
    def initialise(**kwargs) -> StringGene:
        length = kwargs.get('gene_length', 0)

        if length <= 0:
            raise ValueError('gene_length <= 0, no kinder-bueno')

        indices = randint(len(alphabet), size=length)
        return StringGene(string=''.join(map(lambda index: alphabet[index], indices)))