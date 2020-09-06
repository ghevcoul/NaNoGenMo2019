
import math
import random

import svgwrite
from PIL import Image, ImageDraw

from fractal_tree import FractalTree

from typing import Tuple

class SVGWriter:

    def __init__(self, 
        _tree: FractalTree, 
        _filename: str,
        _bark: Tuple[int, int, int], 
        _foliage: Tuple[int, int, int]):
        
        self.tree = _tree
        self.filename = _filename
        self.bark_colour = svgwrite.rgb(*_bark)
        self.foliage_colour = svgwrite.rgb(*_foliage)

        self.svg_img = None

    def generate_svg(self):
        """
        Generates an SVG image from the list of line segments defining a FractalTree
        """
        self.svg_img = svgwrite.Drawing(size=self.tree.get_max_vals())

        # Add each branch to the drawing
        for branch in self.tree.tree:
            if branch.leaf:
                color = self.foliage_colour
            else:
                color = self.bark_colour

            self.svg_img.add(self.svg_img.line(
                start=(branch.line.start.x, branch.line.start.y),
                end=(branch.line.end.x, branch.line.end.y),
                stroke=color,
                stroke_width=branch.width,
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


class PNGWriter:

    def __init__(self, 
        _tree: FractalTree, 
        _filename: str,
        _bark: Tuple[int, int, int], 
        _foliage: Tuple[int, int, int]):

        self.tree = _tree
        self.filename = _filename
        self.bark_colour = _bark
        self.foliage_colour = _foliage

        self.im: Image = None

    
    def generate_image(self) -> None:
        draw = ImageDraw.Draw(self.im)

        # Add each branch to the drawing
        for branch in self.tree.tree:
            if branch.leaf:
                color = self.foliage_colour
            else:
                color = self.bark_colour
            
            draw.line(
                [(branch.line.start.x, branch.line.start.y), (branch.line.end.x, branch.line.end.y)],
                fill=color,
                width=branch.width
            )
    

    def write(self) -> None:
        self.im = Image.new("RGB", size=self.tree.get_max_vals(), color="white")
        self.generate_image()
        self.im.save(self.filename, format="PNG", optimize=True)
