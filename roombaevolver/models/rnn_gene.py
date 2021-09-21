from __future__ import annotations

from core.models import Gene

from typing import Tuple

from numpy import ndarray, zeros
from numpy.random import uniform


class RNNGene(Gene):
    def __init__(self, input_weights: ndarray, recurrent_weights: ndarray):
        self.input_weights: ndarray = input_weights
        self.recurrent_weights: ndarray = recurrent_weights

    def mutate(self, mutation_probability: float):
        # mutation should happen here
        # the same mutation code can be used for both the input_weights and recurrent_weights
        pass

    def crossover(self, other: RNNGene) -> Tuple[RNNGene, RNNGene]:
        # crossover should happen here
        # the same crossover code can be used for both the input_weights and recurrent_weights
        return self, other

    def __repr__(self):
        return "[Gene - input_weights:\n{inputs}, \nrecurrent_weights: \n{recurrent}]".format(inputs=self.input_weights, recurrent=self.recurrent_weights)

    @staticmethod
    def initialise(**kwargs) -> RNNGene:
        inputs = kwargs.get("inputs", 0)
        outputs = kwargs.get("outputs", 0)

        if inputs <= 0 or outputs <= 0:
            pass # TODO raise exception

        # the +1 at inputs is to account for the bias node
        input_weights: ndarray = uniform(low=-1, high=1, size=(inputs + 1, outputs))
        recurrent_weights: ndarray = uniform(low=-1, high=1, size=(outputs, outputs))

        return RNNGene(input_weights, recurrent_weights)
