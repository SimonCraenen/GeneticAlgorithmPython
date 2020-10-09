from ...models import Vehicle, Environment

from numpy import ndarray, zeros

from math import cos, sin, pi

from typing import Set

from traceback import print_exc


class Simulator:
    def __init__(self, environment: Environment, vehicle: Vehicle, timestep: float=.05):
        self.environment: Environment = environment

        width: float = self.environment.upper_x_bound - self.environment.lower_x_bound
        height: float = self.environment.upper_y_bound - self.environment.lower_y_bound
        
        self.vehicle: Vehicle = vehicle

        self.cell_size: float = (self.vehicle.radius / 3)
        self.scoring_grid: ndarray = zeros(shape=(int(height / self.cell_size) + 1, int(width / self.cell_size) + 1))
        self.active_cells: Set = set()

        self.timestep: float = timestep
        self.epsilon: float = 0.00001
        self.collision_count: int = 0

    def start(self, max_simulation_time: int):
        time: float = 0

        while time < max_simulation_time:
            self.__update(self.timestep)
            time += self.timestep

    def __update(self, delta: float):
        self.__update_vehicle(delta)

    def __update_vehicle(self, delta: float):
        self.vehicle.update_sensors(self.environment)
        self.vehicle.update_throttle()

        left_wheel_velocity: float = self.vehicle.motor_input[0] * self.vehicle.speed
        right_wheel_velocity: float = self.vehicle.motor_input[1] * self.vehicle.speed

        new_x: float = self.vehicle.x
        new_y: float = self.vehicle.y
        new_theta: float = self.vehicle.theta

        if abs(left_wheel_velocity - right_wheel_velocity) < self.epsilon:
            new_x = self.vehicle.x + delta * left_wheel_velocity * cos(self.vehicle.theta)
            new_y = self.vehicle.y + delta * left_wheel_velocity * sin(self.vehicle.theta)
        else:
            radius: float = 0

            if abs(left_wheel_velocity + right_wheel_velocity) < self.epsilon:
                radius = 0
            elif abs(left_wheel_velocity) < self.epsilon:
                radius = self.vehicle.radius
            elif abs(right_wheel_velocity) < self.epsilon:
                radius = -self.vehicle.radius
            else:
                radius = self.vehicle.radius * (left_wheel_velocity + right_wheel_velocity) / (right_wheel_velocity - left_wheel_velocity)

            iccx: float = self.vehicle.x - radius * sin(self.vehicle.theta)
            iccy: float = self.vehicle.y + radius * cos(self.vehicle.theta)
            omega: float = (right_wheel_velocity - left_wheel_velocity) / (2 * self.vehicle.radius)

            omega_delta: float = omega * delta

            new_x = cos(omega_delta) * (self.vehicle.x - iccx) - (sin(omega_delta) * (self.vehicle.y - iccy)) + iccx
            new_y = sin(omega_delta) * (self.vehicle.x - iccx) + (cos(omega_delta) * (self.vehicle.y - iccy)) + iccy

            new_theta = self.vehicle.theta + omega_delta
            new_theta += pi * 2
            new_theta = new_theta % (pi * 2)

        collided: bool = False
        for obstacle in self.environment.obstacles:
            if obstacle.find_circle_intersection(new_x, new_y, self.vehicle.radius):
                collided = True
                break

        if not collided:
            self.vehicle.x = new_x
            self.vehicle.y = new_y
            self.vehicle.theta = new_theta

            # store which cells are covered by the vehicle
            lower_x_index = int((self.vehicle.x - self.environment.lower_x_bound - self.vehicle.radius) / self.cell_size)
            upper_x_index = int((self.vehicle.x - self.environment.lower_x_bound + self.vehicle.radius) / self.cell_size)
            lower_y_index = int((self.vehicle.y - self.environment.lower_y_bound - self.vehicle.radius) / self.cell_size)
            upper_y_index = int((self.vehicle.y - self.environment.lower_y_bound + self.vehicle.radius) / self.cell_size)

            new_active_cells: Set = set()
            for j in range(lower_y_index, upper_y_index):
                for i in range(lower_x_index, upper_x_index):
                    new_active_cells.add((j, i))
                    if (j, i) not in self.active_cells:
                        self.scoring_grid[j, i] += 1

            self.active_cells = new_active_cells
        else:
            self.collision_count += 1
