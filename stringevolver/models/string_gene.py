from __future__ import annotations

from core.models import Gene

from typing import Tuple

from numpy.random import randint
from numpy import where
from random import choices as rand_choices

from abc import abstractmethod, abstractstaticmethod


alphabet = "abcdefghijklmnopqrstuvwxyz -"

class StringGene(Gene):
    def __init__(self, string: str):
        self.string = string

    def mutate(self, mutation_probability: float):
        should_mutate = rand_choices(population=[True, False], weights=[mutation_probability, 1-mutation_probability], k=len(self.string))
        for i in range(len(self.string)):
            if not should_mutate[i]:
                continue

            self.string = self.string[:i] + alphabet[int(randint(len(alphabet)))] + self.string[i + 1:]

    def crossover(self, other: StringGene) -> Tuple[StringGene, StringGene]:
        crossover_point = int(len(self.string) / 2)
        return (StringGene(self.string[:crossover_point] + other.string[crossover_point:]), StringGene(other.string[:crossover_point] + self.string[crossover_point:]))

    def __repr__(self):
        return "[Gene - {string}]".format(string=self.string)

    @staticmethod
    def initialise(**kwargs) -> StringGene:
        length = kwargs.get("gene_length", 0)

        if length == 0:
            pass # TODO raise exception

        indices = randint(len(alphabet), size=length)
        return StringGene(string="".join(map(lambda index: alphabet[index], indices)))