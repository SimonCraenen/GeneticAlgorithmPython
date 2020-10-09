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

        return 0
