from __future__ import annotations

from math import sqrt


class LineSegment:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1: float = x1
        self.y1: float = y1

        self.x2: float = x2
        self.y2: float = y2

    def find_segment_intersection(self, other: LineSegment):
        s1_x: float = self.x2 - self.x1
        s1_y: float = self.y2 - self.y1

        s2_x: float = other.x2 - other.x1
        s2_y: float = other.y2 - other.y1

        denominator: float = (-s2_x * s1_y + s1_x * s2_y)

        if denominator == 0:
            denominator += 0.000001

        s: float = (-s1_y * (self.x1 - other.x1) + s1_x * (self.y1 - other.y1)) / denominator
        t: float = (s2_x * (self.y1 - other.y1) - s2_y * (self.x1 - other.x1)) / denominator

        if 0 < s < 1 and 0 < t < 1:
            return True, (self.x1 + (t * s1_x), self.y1 + (t * s1_y))

        return False, None

    def find_circle_intersection(self, center_x: float, center_y: float, radius: float) -> bool:
        s1_x: float = self.x2 - self.x1
        s1_y: float = self.y2 - self.y1

        s2_x: float = center_x - self.x1
        s2_y: float = center_y - self.y1

        a: float = s1_x ** 2 + s1_y ** 2
        b_by_2: float = s1_x * s2_x + s1_y * s2_y
        c: float = s2_x ** 2 + s2_y ** 2 - radius ** 2

        p_by_2: float = b_by_2 / a
        q: float = c / a

        disc: float = p_by_2 ** 2 - q
        if disc < 0:
            return False

        temp_sqrt: float = sqrt(disc)
        ab_scaling_factor_one: float = -p_by_2 + temp_sqrt
        ab_scaling_factor_two: float = -p_by_2 - temp_sqrt\

        intersect_x_one = self.x1 - s1_x * ab_scaling_factor_one
        intersect_y_one = self.y1 - s1_y * ab_scaling_factor_one

        lower_x_bound = min(self.x1, self.x2)
        upper_x_bound = max(self.x1, self.x2)
        lower_y_bound = min(self.y1, self.y2)
        upper_y_bound = max(self.y1, self.y2)

        if disc == 0:
            if (lower_x_bound <= intersect_x_one <= upper_x_bound) and (lower_y_bound <= intersect_y_one <= upper_y_bound):
                return True
            else:
                return False
        else:
            if (lower_x_bound <= intersect_x_one <= upper_x_bound) and (lower_y_bound <= intersect_y_one <= upper_y_bound):
                return True

            intersect_x_two = self.x1 - s1_x * ab_scaling_factor_two
            intersect_y_two = self.y1 - s1_y * ab_scaling_factor_two

            if (lower_x_bound <= intersect_x_two <= upper_x_bound) and (lower_y_bound <= intersect_y_two <= upper_y_bound):
                return True

            return False
