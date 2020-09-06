
import math
import random

import svgwrite

from fractal_tree import FractalTree

from typing import Tuple

class SVGWriter:

    def __init__(self, 
        _tree: FractalTree, 
        _filename: str,
        _bark: Tuple[int, int, int], 
        _foliage: Tuple[int, int, int],
        _foliage_length: int):
        
        self.tree = _tree
        self.filename = _filename
        self.bark_colour = svgwrite.rgb(*_bark)
        self.foliage_colour = svgwrite.rgb(*_foliage)
        self.foliage_length = _foliage_length

        self.svg_img = None

    def generate_svg(self):
        """
        Generates an SVG image from the list of line segments defining a FractalTree
        """
        self.svg_img = svgwrite.Drawing(size=self.tree.get_max_vals())

        # Add each branch to the drawing
        for branch in self.tree.tree:
            width = math.floor(branch.length() / random.randint(6, 9))
            if width < 1:
                width = 1

            if branch.length() >= self.foliage_length:
                color = self.bark_colour
            else:
                color = self.foliage_colour

            self.svg_img.add(self.svg_img.line(
                start=(branch.start.x, branch.start.y),
                end=(branch.end.x, branch.end.y),
                stroke=color,
                stroke_width=width,
                stroke_linecap="round"
            ))


    def write(self):
        """
        Write SVG to filename.
        """
        if not self.svg_img:
            self.generate_svg()
        self.svg_img.saveas(self.filename, pretty=True, indent=2)


    def get_svg_string(self) -> str:
        """
        Returns the SVG image as a string.
        """
        if not self.svg_img:
            self.generate_svg()
        return self.svg_img.tostring()
