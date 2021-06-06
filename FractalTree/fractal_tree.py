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


@dataclass
class Branch:

    line: LineSegment
    width: int
    leaf: bool


class FractalTree:
    """
    A class for building randomized fractal trees.
    """
    def __init__(self):
        self.trunk_length: int = 100
        self.start_angle: int = 270
        self.start_pos: Point = Point(0, 0)

        self.tree: List[Branch] = []


    def generate(self):
        """
        Generate a tree using the parameters set in the constructor.
        Calls a recursive function that actually does the tree building with the starting values
        """
        self._build_tree(self.start_pos, self.trunk_length, self.start_angle)


    def _build_tree(self, start: Point, branch_len: float, branch_angle: float) -> None:
        """
        Empty base function to be overridden in extending classes
        """
        pass


    def get_max_vals(self) -> Tuple[int, int]:
        """
        Finds the max x and y values in the given tree and returns them.
        """
        x_vals = [(branch.line.start.x, branch.line.end.x) for branch in self.tree]
        x_vals = [item for sublist in x_vals for item in sublist]
        y_vals = [(branch.line.start.y, branch.line.end.y) for branch in self.tree]
        y_vals = [item for sublist in y_vals for item in sublist]

        return int(math.ceil(max(x_vals))), int(math.ceil(max(y_vals)))


    def normalize(self):
        """
        Normalizes the tree by making all coordinates positive.
        """
        # Find the minimum x and y values
        x_vals = [(branch.line.start.x, branch.line.end.x) for branch in self.tree]
        x_vals = [item for sublist in x_vals for item in sublist]
        y_vals = [(branch.line.start.y, branch.line.end.y) for branch in self.tree]
        y_vals = [item for sublist in y_vals for item in sublist]
        x_shift = abs(min(x_vals))
        y_shift = abs(min(y_vals))

        # Add the shift values to each point
        for branch in self.tree:
            new_segment = LineSegment(
                Point(branch.line.start.x + x_shift, branch.line.start.y + y_shift),
                Point(branch.line.end.x + x_shift, branch.line.end.y + y_shift)
            )
            branch.line = new_segment


class DeciduousTree(FractalTree):

    def __init__(self):
        super().__init__()

        self.trunk_length: int = 150

        # Will the tree be symmetrical? 65% chance of asymmetry
        #TODO: Implement symmetrical trees
        self.symmetrical: bool = random.random() > 0.65
        # What fraction will the length of the next branch be reduced
        self.length: Tuple[float, float] = (0.45, 0.85)
        # What angle (in degrees) will the next branch have
        self.angle: Tuple[int, int] = (-65, 65)
        # How many branches will come off this branch
        self.branches: List[int] = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]
        # How short does a branch have to be to be considered a leaf
        self.leaf_length = random.randint(5, 25)


    def _build_tree(self, start: Point, branch_len: float, branch_angle: float) -> None:
        """
        Recursively build the tree, exiting when the branch length is 3 or less.
        """
        if branch_len > 3:
            branch = self._make_branch(start, branch_len, branch_angle)
            self.tree.append(branch)

            for _ in range(random.choice(self.branches)):
                self._build_tree(
                    branch.line.end,
                    branch_len * random.uniform(self.length[0], self.length[1]),
                    branch_angle + random.randrange(self.angle[0], self.angle[1])
                )


    def _make_branch(self, start: Point, branch_length: float, branch_angle: float) -> Branch:
        """
        Gets the xy coordinates for the end of a branch with the input starting coordinates
        with branch length and angle.
        Returns a LineSegment
        """
        end_point = Point(
            start.x + (branch_length * math.cos(math.radians(branch_angle))),
            start.y + (branch_length * math.sin(math.radians(branch_angle)))
        )
        segment = LineSegment(start, end_point)

        width = math.floor(segment.length() / random.randint(6, 9))
        if width < 1:
            width = 1
        
        leaf = segment.length() <= self.leaf_length

        return Branch(segment, width, leaf)


if __name__ == "__main__":
    # random.seed(1234)
    TREE = FractalTree()
    TREE.generate()
