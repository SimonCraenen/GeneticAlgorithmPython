from .environment import Environment
from .sensor import Sensor
from ..network import RNN

from math import pi

from numpy import array, ndarray

from typing import List


class Vehicle:
    def __init__(self, radius: float, sensor_amount: int, sensor_range: float, speed: float=1.0, network: RNN=None):
        self.network: RNN = network

        self.speed : float = speed

        self.radius: float = radius

        self.sensor_amount: int = sensor_amount
        self.sensor_range: float = sensor_range

        self.sensors: List[Sensor] = [Sensor(theta=(i * pi * 2 / self.sensor_amount), reach=self.sensor_range) for i in range(self.sensor_amount)]

        self.x: float = 0
        self.y: float = 0
        self.theta: float = 0

        self.motor_input: ndarray = array([.5, .5])

    def update_sensors(self, environment: Environment):
        for sensor in self.sensors:
            sensor.update(self.x, self.y, self.theta, self.radius, environment)

    def update_throttle(self):
        self.motor_input = self.network.feed_forward(array([sensor.value for sensor in self.sensors]))

        