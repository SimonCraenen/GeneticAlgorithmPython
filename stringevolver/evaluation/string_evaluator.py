from core.algorithm.evaluation import Evaluator
from core.models import Individual

from stringevolver.models import StringGene

class StringEvaluator(Evaluator):
    def __init__(self, target: str):
        super().__init__()

        self.target = target

    def evaluate(self, individual: Individual) -> float:
        gene: StringGene = individual.gene

        # safety check, should never happen
        if len(self.target) != len(gene.string):
            return 0

        # return the percentage (0,1) of characters that overlap between the gene and the target

        return 0
