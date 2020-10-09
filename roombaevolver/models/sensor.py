from .line_segment import LineSegment
from .environment import Environment

from math import sin, cos, sqrt


class Sensor:
    def __init__(self, theta: float, reach: float):
        self.theta: float = theta
        self.reach: float = reach

        self.value: float = 0

        self.segment: LineSegment = LineSegment(0, 0, 0, 0)

    def update(self, x: float, y: float, vehicle_theta: float, vehicle_radius: float, environment: Environment) -> float:
        theta: float = self.theta + vehicle_theta
        
        cos_theta = cos(theta)
        sin_theta = sin(theta)

        self.segment.x1 = x + vehicle_radius * cos_theta
        self.segment.y1 = y + vehicle_radius * sin_theta
        self.segment.x2 = x + (vehicle_radius + self.reach) * cos_theta
        self.segment.y2 = y + (vehicle_radius + self.reach) * sin_theta

        closest_intersection = self.reach

        for obstacle in environment.obstacles:
            intersects, intersection = self.segment.find_segment_intersection(obstacle)

            if intersects:
                distance = sqrt((intersection[0] - self.segment.x1) ** 2 + (intersection[1] - self.segment.y1) ** 2)
                if distance < closest_intersection:
                    closest_intersection = distance

        self.value = (self.reach - closest_intersection) / self.reach

        return self.value
