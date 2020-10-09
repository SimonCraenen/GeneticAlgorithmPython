from .line_segment import LineSegment

from typing import Tuple, List


class Environment:
    def __init__(self, obstacles: List[LineSegment]):
        self.obstacles = obstacles

        self.lower_x_bound = min(min([obstacle.x1 for obstacle in self.obstacles]), min([obstacle.x2 for obstacle in self.obstacles]))
        self.upper_x_bound = max(max([obstacle.x1 for obstacle in self.obstacles]), max([obstacle.x2 for obstacle in self.obstacles]))
        self.lower_y_bound = min(min([obstacle.y1 for obstacle in self.obstacles]), min([obstacle.y2 for obstacle in self.obstacles]))
        self.upper_y_bound = max(max([obstacle.y1 for obstacle in self.obstacles]), max([obstacle.y2 for obstacle in self.obstacles]))


MAZE = Environment([
    LineSegment(0, 0, 5, 0),
    LineSegment(0, 0, 0, 5),
    LineSegment(5, 0, 5, 5),
    LineSegment(0, 5, 5, 5),
    LineSegment(4, 5, 4, 1),
    LineSegment(3, 0, 3, 4),
    LineSegment(2, 1, 2, 3),
    LineSegment(2, 4, 2, 5),
    LineSegment(1, 1, 2, 1),
    LineSegment(0, 2, 1, 2),
    LineSegment(1, 3, 1, 4),
    LineSegment(1, 3, 3, 3)
])

KAMI = Environment([
    LineSegment(.25, 4.75, 4.75, 4.75),
    LineSegment(.25, .25, 3, .25),
    LineSegment(.25, .25, .25, 4.75),
    LineSegment(4.75, .25, 4.75, 4.75),
    LineSegment(4, .25, 4.75, .25),
    LineSegment(1, .25, 1, 3.5),
    LineSegment(1, 3.5, 2, 3.5),
    LineSegment(2, 3.5, 2, 2.5),
    LineSegment(2, 2.5, 3.5, 2.5),
    LineSegment(3.9, 2.5, 4, 2.5),
    LineSegment(4, 2.5, 4, 3.5),
    LineSegment(4, 3.5, 4.75, 3.5),
    LineSegment(2.25, 2.1, 2.25, 1),
    LineSegment(3.6, 2.1, 3.6, 1),
])

KAMI_V2 = Environment([
    LineSegment(1, 2, 1, 6),
    LineSegment(1, 6, 3, 6),
    LineSegment(1, 2, 3, 2),
    LineSegment(3, 1, 3, 3),
    LineSegment(3, 4, 3, 7),
    LineSegment(3, 1, 6, 1),
    LineSegment(8, 1, 11, 1),
    LineSegment(3, 7, 11, 7),
    LineSegment(11, 1, 11, 3),
    LineSegment(11, 4, 11, 7),
    LineSegment(11, 2, 13, 2),
    LineSegment(13, 2, 13, 6),
    LineSegment(6, 3, 6, 4),
    LineSegment(8, 3, 8, 4),
    LineSegment(6, 3, 8, 3),
    LineSegment(6, 4, 8, 4),
    LineSegment(5, 2, 5, 3),
    LineSegment(5, 2, 9, 2),
    LineSegment(9, 2, 9, 3),
    LineSegment(7, 2, 7, 3),
    LineSegment(5, 5, 5, 6),
    LineSegment(9, 5, 9, 6),
    LineSegment(11, 6, 13, 6),

    LineSegment(.1, .5, .1, 7.5),
    LineSegment(.1, .5, 13.5, .5),
    LineSegment(.1, 7.5, 13.5, 7.5),
    LineSegment(13.5, .5, 13.5, 7.5),
])
