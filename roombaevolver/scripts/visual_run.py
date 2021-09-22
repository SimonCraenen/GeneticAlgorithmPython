from sys import path as sys_path

sys_path.append("./")

from roombaevolver.evaluation.simulation.visual_simulator import VisualSimulator
from roombaevolver.models import Environment, MAZE, KAMI, KAMI_V2
from roombaevolver.models import RNNGene, Vehicle
from roombaevolver.network import RNN

from numpy import append

from math import pi

from kivy.app import App
from kivy.core.window import Window

from threading import Thread

from pickle import load as pickle_load


class Container(App):
    def __init__(self, simulator: VisualSimulator):
        super().__init__()

        Window.size = (1920, 1080)
        Window.top = 0
        Window.left = 0

        self.simulator: VisualSimulator = simulator

    def build(self):
        Window.clearcolor = (0.93, 0.93, 0.93, 1)
        return self.simulator

if __name__ == "__main__":
    individual = pickle_load(open('results/roombaevolver/best-individual-generation-{generation}.p'.format(generation=1), 'rb'))

    gene: RNNGene = individual.gene

    network: RNN = RNN(input_weights=gene.input_weights, recurrent_weights=gene.recurrent_weights)

    vehicle: Vehicle = Vehicle(radius=0.17, sensor_amount=12, sensor_range=1.5, speed=1, network=network)
    vehicle.x = 6.5
    vehicle.y = .75
    vehicle.theta = pi / 2

    environment: Environment = KAMI_V2

    vehicle.update_sensors(environment)

    simulator: VisualSimulator = VisualSimulator(environment, vehicle, enable_keyboard=False)

    thread = Thread(target=simulator.start, args=(200,))
    thread.start()
    
    container = Container(simulator)
    container.run()
