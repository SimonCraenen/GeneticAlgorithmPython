from core.algorithm.evaluation import Evaluator
from core.models import Individual

from stringevolver.models import StringGene

class StringEvaluator(Evaluator):
    def __init__(self, target: str):
        super().__init__()

        self.target = target

    def evaluate(self, individual: Individual) -> int:
        gene: StringGene = individual.gene

        if len(self.target) != len(gene.string):
            return 0

        return sum([1 if gene.string[i] == self.target[i] else 0 for i in range(len(self.target))]) / len(self.target)
