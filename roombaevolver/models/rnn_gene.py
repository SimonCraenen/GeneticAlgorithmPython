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
        input_weights_shape = self.input_weights.shape
        recurrent_weights_shape = self.recurrent_weights.shape

        for j in range(input_weights_shape[0]):
            for i in range(input_weights_shape[1]):
                if uniform() < mutation_probability:
                    self.input_weights[j, i] = uniform(low=-1, high=1)

        for j in range(recurrent_weights_shape[0]):
            for i in range(recurrent_weights_shape[1]):
                if uniform() < mutation_probability:
                    self.recurrent_weights[j, i] = uniform(low=-1, high=1)

    def crossover(self, other: RNNGene) -> Tuple[RNNGene, RNNGene]:
        return self.alternating_crossover(other)

    def alternating_crossover(self, other: RNNGene) -> Tuple[RNNGene, RNNGene]:
        input_weights_shape = self.input_weights.shape

        child_one_input_weights = zeros(shape=input_weights_shape)
        child_two_input_weights = zeros(shape=input_weights_shape)

        for j in range(input_weights_shape[0]):
            for i in range(input_weights_shape[1]):
                idx = i + j * input_weights_shape[1]

                if idx % 2 == 0:
                    child_one_input_weights[j, i] = self.input_weights[j, i]
                    child_two_input_weights[j, i] = other.input_weights[j, i]
                else:
                    child_one_input_weights[j, i] = other.input_weights[j, i]
                    child_two_input_weights[j, i] = self.input_weights[j, i]

        recurrent_weights_shape = self.recurrent_weights.shape

        child_one_recurrent_weights = zeros(shape=recurrent_weights_shape)
        child_two_recurrent_weights = zeros(shape=recurrent_weights_shape)

        for j in range(recurrent_weights_shape[0]):
            for i in range(recurrent_weights_shape[1]):
                idx = i + j * recurrent_weights_shape[1]

                if idx % 2 == 0:
                    child_one_recurrent_weights[j, i] = self.recurrent_weights[j, i]
                    child_two_recurrent_weights[j, i] = other.recurrent_weights[j, i]
                else:
                    child_one_recurrent_weights[j, i] = other.recurrent_weights[j, i]
                    child_two_recurrent_weights[j, i] = self.recurrent_weights[j, i]

        return (RNNGene(child_one_input_weights, child_one_recurrent_weights), RNNGene(child_two_input_weights, child_two_recurrent_weights))        

    def __repr__(self):
        return "[Gene - input_weights:\n{inputs}, \nrecurrent_weights: \n{recurrent}]".format(inputs=self.input_weights, recurrent=self.recurrent_weights)

    @staticmethod
    def initialise(**kwargs) -> RNNGene:
        inputs = kwargs.get("inputs", 0)
        outputs = kwargs.get("outputs", 0)

        if inputs <= 0 or outputs <= 0:
            pass # TODO raise exception

        # the +1 at inputs is the account for the bias node
        input_weights: ndarray = uniform(low=-1, high=1, size=(inputs + 1, outputs))
        recurrent_weights: ndarray = uniform(low=-1, high=1, size=(outputs, outputs))

        return RNNGene(input_weights, recurrent_weights)
