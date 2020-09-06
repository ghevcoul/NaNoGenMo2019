
import math
import random

import svgwrite

import colours
from fractal_tree import FractalTree


class EntryWriter:
    """
    Generate and write an entry into the field guide.
    """
    def __init__(self):
        self.tree: FractalTree = FractalTree()
        self.bark_colour = None
        self.bark_colour_name: str = None
        self.foliage_colour = None
        self.foliage_colour_name: str = None

        self._select_bark_colour()
        self._select_foliage_colour()

        self.foliage_length = random.randint(5, 25)


    def generate_svg(self):
        """
        Generates an SVG image from the list of line segments defining a FractalTree
        """
        # First build the tree
        self.tree.generate()
        self.tree.normalize()

        self.svg_img = svgwrite.Drawing(size=self.tree.get_max_vals())

        # Add each branch to the drawing
        for branch in self.tree.tree:
            width = math.floor(branch.length() / 8)
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


    def write_file(self, filename):
        """
        Write SVG to filename.
        """
        if filename[-4:] != ".svg":
            filename += ".svg"

        self.svg_img.saveas(filename, pretty=True, indent=2)


    def get_svg_string(self) -> str:
        """
        Returns the SVG image as a string.
        """
        return self.svg_img.tostring()


    def _select_bark_colour(self) -> None:
        """
        Chooses the colour of the trunk of the tree. Saves the colour to the class as an RGB and a string naming the colour.

        70% chance of choosing a brown trunk, 30% chance of choosing a gray/silver
        """
        colour_selector = random.random()
        if colour_selector <= 0.70:
            colour = random.choice(colours.BROWNS)
            self.bark_colour = svgwrite.rgb(*colour)
            self.bark_colour_name = "brown"
        else:
            colour = random.choice(colours.GRAYS)
            self.bark_colour = svgwrite.rgb(*colour)
            self.bark_colour_name = random.choice(["silver", "gray", "grey"])
        
        print(f"Selected {self.bark_colour_name} bark with colour {colour}")
    
    def _select_foliage_colour(self) -> None:
        """
        Chooses the colour of the foliage for the tree. Saves the colour to the class as an RGB and a string naming the colour.

        80% chance of choosing green leaves, 10% chance each of choosing ornamental or flowering
        """
        colour_selector = random.random()
        if colour_selector <= 0.80:
            colour = random.choice(colours.GREENS)
            self.foliage_colour = svgwrite.rgb(*colour)
            self.foliage_colour_name = "green"
        elif 0.80 < colour_selector <= 0.90:
            colour = random.choice(colours.ORNAMENTAL)
            self.foliage_colour = svgwrite.rgb(*colour)
            self.foliage_colour_name = "ornamental"
        else:
            colour = random.choice(colours.FLOWERING)
            self.foliage_colour = svgwrite.rgb(*colour)
            self.foliage_colour_name = "flowering"
        
        print(f"Selected {self.foliage_colour_name} leaves with colour {colour}")


if __name__ == "__main__":
    entry = EntryWriter()
    entry.generate_svg()
    entry.write_file("test.svg")
