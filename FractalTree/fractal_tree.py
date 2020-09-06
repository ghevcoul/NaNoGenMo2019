"""
A recursive fractal tree builder.
"""
import math
import random
from dataclasses import dataclass

from typing import List, Tuple


@dataclass
class Point:
    """
    Cartesian point
    """
    x: float
    y: float


@dataclass
class LineSegment:
    """
    Line segment defined by two pairs of Cartesian xy coordinates
    """
    start: Point
    end: Point

    def length(self) -> float:
        """
        Calculates the length of the LineSegment
        """
        return math.sqrt((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)


class FractalTree:
    """
    A class for building randomized fractal trees.
    """
    def __init__(self):
        self.trunk_length: int = 150
        self.start_angle: int = 270
        self.start_pos: Point = Point(0, 0)

        # Will the tree be symmetrical? 65% chance of asymmetry
        #TODO: Implement symmetrical trees
        self.symmetrical: bool = random.random() > 0.65
        # What fraction will the length of the next branch be reduced
        self.length: Tuple[float, float] = (0.45, 0.85)
        # What angle (in degrees) will the next branch have
        self.angle: Tuple[int, int] = (-65, 65)
        # How many branches will come off this branch
        self.branches: List[int] = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]

        self.tree: List[LineSegment] = []

    def generate(self):
        """
        Generate a tree using the parameters set in the constructor.
        Calls a recursive function that actually does the tree building with the starting values
        """
        self._build_tree(self.start_pos, self.trunk_length, self.start_angle)

    def get_max_vals(self) -> Tuple[float, float]:
        """
        Finds the max x and y values in the given tree and returns them.
        """
        x_vals = [(line.start.x, line.end.x) for line in self.tree]
        x_vals = [item for sublist in x_vals for item in sublist]
        y_vals = [(line.start.y, line.end.y) for line in self.tree]
        y_vals = [item for sublist in y_vals for item in sublist]

        return math.ceil(max(x_vals)), math.ceil(max(y_vals))

    def normalize(self):
        """
        Normalizes the tree by making all coordinates positive.
        """
        # Find the minimum x and y values
        x_vals = [(line.start.x, line.end.x) for line in self.tree]
        x_vals = [item for sublist in x_vals for item in sublist]
        y_vals = [(line.start.y, line.end.y) for line in self.tree]
        y_vals = [item for sublist in y_vals for item in sublist]
        x_shift = abs(min(x_vals))
        y_shift = abs(min(y_vals))

        # Add the shift values to each point
        new_tree = []
        for line in self.tree:
            new_segment = LineSegment(
                Point(line.start.x + x_shift, line.start.y + y_shift),
                Point(line.end.x + x_shift, line.end.y + y_shift)
            )
            new_tree.append(new_segment)

        self.tree = new_tree

    def _build_tree(self, start: Point, branch_len: float, branch_angle: float):
        """
        Recursively build the tree, exiting when the branch length is 3 or less.
        """
        if branch_len > 3:
            branch = self._make_branch(start, branch_len, branch_angle)
            self.tree.append(branch)

            for _ in range(random.choice(self.branches)):
                self._build_tree(
                    branch.end,
                    branch_len * random.uniform(self.length[0], self.length[1]),
                    branch_angle + random.randrange(self.angle[0], self.angle[1])
                )

    @staticmethod
    def _make_branch(start: Point, branch_length: float, branch_angle: float) -> LineSegment:
        """
        Gets the xy coordinates for the end of a branch with the input starting coordinates
        with branch length and angle.
        Returns a LineSegment
        """
        end_point = Point(
            start.x + (branch_length * math.cos(math.radians(branch_angle))),
            start.y + (branch_length * math.sin(math.radians(branch_angle)))
        )
        return LineSegment(start, end_point)



if __name__ == "__main__":
    # random.seed(1234)
    TREE = FractalTree()
    TREE.generate()
