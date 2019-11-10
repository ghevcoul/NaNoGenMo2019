
import math

import svgwrite

from fractal_tree import FractalTree


class EntryWriter:
    """
    Generate and write an entry into the field guide.
    """
    def __init__(self):
        self.tree: FractalTree = FractalTree()

        self.trunk_color = svgwrite.rgb(139, 69, 19)
        self.foliage_color = svgwrite.rgb(34, 139, 34)

        self.foliage_length = 6

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
                color = self.trunk_color
            else:
                color = self.foliage_color

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


if __name__ == "__main__":
    entry = EntryWriter()
    entry.generate_svg()
    entry.write_file("test.svg")
