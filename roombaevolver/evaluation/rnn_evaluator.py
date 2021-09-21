from core.algorithm.evaluation import Evaluator
from core.models import Individual

from ..models import RNNGene, Vehicle, Environment
from ..network import RNN
from ..evaluation.simulation import Simulator

from numpy import ndarray

from typing import Tuple


class RNNEvaluator(Evaluator):
    def __init__(self, environment: Environment, starting_location: Tuple[float, float, float], vehicle_radius: float=.17, sensor_range: float=1.5, simulation_time: float=45):
        super().__init__()

        self.starting_location: Tuple[float, float, float] = starting_location
        self.vehicle_radius: float = vehicle_radius
        self.sensor_range: float = sensor_range
        self.simulation_time: float = simulation_time
        self.environment: Environment = environment

    def evaluate(self, individual: Individual) -> float:
        gene: RNNGene = individual.gene

        network: RNN = RNN(input_weights=gene.input_weights, recurrent_weights=gene.recurrent_weights)

        vehicle: Vehicle = Vehicle(radius=self.vehicle_radius, sensor_amount=network.input_weights.shape[0] - 1, sensor_range=self.sensor_range, network=network)
        vehicle.x = self.starting_location[0]
        vehicle.y = self.starting_location[1]
        vehicle.theta = self.starting_location[2]
        vehicle.update_sensors(self.environment)

        simulator: Simulator = Simulator(self.environment, vehicle)

        simulator.start(max_simulation_time=self.simulation_time)

        scoring_grid: ndarray = simulator.scoring_grid

        fitness: float = 0.0
        
        for j in range(scoring_grid.shape[0]):
            for i in range(scoring_grid.shape[1]):
                value = scoring_grid[j, i]

                if value == 0:
                    continue
                else:
                    fitness += 1.0 / value

        fitness /= (scoring_grid.shape[0] * scoring_grid.shape[1])

        individual.data["scoring_grid"] = scoring_grid
        individual.data["score"] = fitness

        return fitness