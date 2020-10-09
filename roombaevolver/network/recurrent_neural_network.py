from __future__ import annotations

from numpy.random import uniform
from numpy import ndarray, array, exp, add, append


class RNN:
    def __init__(self, input_weights: ndarray, recurrent_weights: ndarray):
        self.recurrent_weights: ndarray = recurrent_weights
        self.input_weights: ndarray = input_weights
        self.output_state: ndarray = array([uniform() for _ in range(recurrent_weights.shape[0])])

        self.activation_function = lambda x, lower_bound=-1, upper_bound=1: RNN.__sigmoid_range_map(x, lower_bound, upper_bound)

    def feed_forward(self, inputs: ndarray) -> ndarray:
        """Neural network inference

        Arguments:
        inputs -- a single row with the same amount of columns as rows in the input_weights array

        Returns:
        ndarray -- the new RNN output state
        """

        # add the bias node
        inputs = append(inputs, 1)

        self.output_state = add(self.output_state.dot(self.recurrent_weights), inputs.dot(self.input_weights))
        self.output_state = array(list(map(self.activation_function, self.output_state)))

        return self.output_state

    @staticmethod
    def __sigmoid(x: float) -> float:
        return 1 / (1 + exp(-x))

    @staticmethod
    def __sigmoid_range_map(x: float, lower_bound: float, upper_bound: float) -> float:
        delta = upper_bound - lower_bound
        return 1 / (1 + exp(-x)) * delta + lower_bound
