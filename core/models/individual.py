from __future__ import annotations

from typing import Tuple, Type

from .gene import Gene


class Individual:
    def __init__(self, gene: Gene, fitness: float = -1):
        self.gene: Gene = gene
        self.fitness: float = fitness
        self.data = {}

    def mutate(self, mutation_probability: float):
        self.gene.mutate(mutation_probability)

    def crossover(self, other: Individual) -> Tuple[Individual, Individual]:
        gene_one, gene_two = self.gene.crossover(other.gene)
        return Individual(gene=gene_one), Individual(gene=gene_two)

    @staticmethod
    def initialise(gene_type: Type[Gene], **kwargs) -> Individual:
        return Individual(gene=gene_type.initialise(**kwargs))

    def __repr__(self):
        return "[Individual - gene: {gene}, fitness: {fitness}]".format(gene=self.gene.__str__(), fitness=self.fitness)