from ...models import Vehicle, Environment

from math import cos, sin, pi

from numpy import ndarray, array

from time import time as current_time
from time import sleep

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle, Line, Ellipse, Color

from typing import Dict


class VisualSimulator(Widget):
    def __init__(self, environment: Environment, vehicle: Vehicle, timestep: float=-1, fps: int=60, enable_keyboard: bool=False):
        super().__init__()

        self.enable_keyboard = enable_keyboard

        if self.enable_keyboard:
            self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
            self._keyboard.bind(on_key_down=self._on_keyboard_down)
            self._keyboard.bind(on_key_up=self._on_keyboard_up)
            self._pressed_keys: Dict[str, bool] = {char: False for char in ["w", "a", "s", "d", "q", "e"]}

        self.environment: Environment = environment

        self.vehicle: Vehicle = vehicle

        self.timestep: float = timestep
        self.epsilon: float = 0.00001
        self.scale: float = 130
        self.fps: int = fps

        with self.canvas:
            Color(0, 0, 0, 1)
            self.obstacle_walls = [Line(points=(obstacle.x1 * self.scale, obstacle.y1 * self.scale, obstacle.x2 * self.scale, obstacle.y2 * self.scale)) for obstacle in self.environment.obstacles]
            Color(0, 0, 1, 1)
            self.vehicle_circle = Ellipse(pos=((self.vehicle.x - self.vehicle.radius) * self.scale, (self.vehicle.y - self.vehicle.radius) * self.scale), size=(self.vehicle.radius * 2 * self.scale, self.vehicle.radius * 2 * self.scale))
            Color(.2, .2, .2, .8)
            self.sensor_lines = [Line(points=((sensor.segment.x1 + self.vehicle.x) * self.scale, (sensor.segment.y1 + self.vehicle.y) * self.scale, (sensor.segment.x2 + self.vehicle.x) * self.scale, (sensor.segment.y2 + self.vehicle.y) * self.scale)) for sensor in self.vehicle.sensors]
            Color(1, 0, 0, .8)
            self.vehicle_orientation_line = Line(points=(self.vehicle.x * self.scale, self.vehicle.y * self.scale, (self.vehicle.sensors[0].segment.x1 + self.vehicle.x) * self.scale, (self.vehicle.sensors[0].segment.y1 + self.vehicle.y) * self.scale), width=2)


    def start(self, max_simulation_time: int):
        time: float = 0

        render_delta_threshold: float = 1.0 / self.fps

        previous_render_time: float = current_time()
        previous_update_time: float = current_time()
        while time < max_simulation_time:
            now_time: float = current_time()
            update_delta: float = now_time - previous_update_time if self.timestep <= 0 else self.timestep


            render_delta: float = now_time - previous_render_time
            if render_delta > render_delta_threshold:
                self._update(render_delta)
                self._render()
                previous_render_time = now_time
            else:
                sleep(render_delta_threshold - render_delta)

            previous_update_time = now_time
            time += update_delta

    def _update(self, delta: float):
        self._update_vehicle(delta)

    def _render(self):
        for index, obstacle in enumerate(self.environment.obstacles):
            self.obstacle_walls[index].points = (obstacle.x1 * self.scale, obstacle.y1 * self.scale, obstacle.x2 * self.scale, obstacle.y2 * self.scale)

        self.vehicle_circle.pos = ((self.vehicle.x - self.vehicle.radius) * self.scale, (self.vehicle.y - self.vehicle.radius) * self.scale)

        for index, sensor in enumerate(self.vehicle.sensors):
            self.sensor_lines[index].points = (sensor.segment.x1 * self.scale, sensor.segment.y1 * self.scale, (sensor.segment.x1 + (1 - sensor.value) * sensor.reach * cos(sensor.theta + self.vehicle.theta)) * self.scale, (sensor.segment.y1 + (1 - sensor.value) * sensor.reach * sin(sensor.theta + self.vehicle.theta)) * self.scale)

        self.vehicle_orientation_line.points = (self.vehicle.x * self.scale, self.vehicle.y * self.scale, (self.vehicle.sensors[0].segment.x1) * self.scale, (self.vehicle.sensors[0].segment.y1) * self.scale)

    def _update_vehicle(self, delta: float):
        self.vehicle.update_sensors(self.environment)
        if not self.enable_keyboard:
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

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] not in self._pressed_keys:
            return

        self._pressed_keys[keycode[1]] = True
        self._update_throttle()

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] not in self._pressed_keys:
            return

        self._pressed_keys[keycode[1]] = False
        self._update_throttle()

    def _update_throttle(self):
        motor_input: ndarray = array([0, 0])

        if self._pressed_keys["q"]:
            self.vehicle.motor_input = array([-.5, .5])
            return
        if self._pressed_keys["e"]:
            self.vehicle.motor_input = array([.5, -.5])
            return

        multiplier: float = 1.0
        if self._pressed_keys["w"]:
            motor_input = array([.5, .5])
        elif self._pressed_keys["s"]:
            multiplier = -1.0
            motor_input = array([-.5, -.5])

        if self._pressed_keys["d"]:
            motor_input = array([motor_input[0] + multiplier * .5, motor_input[1]])
        if self._pressed_keys["a"]:
            motor_input = array([motor_input[0], motor_input[1] + multiplier * .5])

        self.vehicle.motor_input = motor_input

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None