
import math
import random

import svgwrite

import colours
import names
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
        self.tree_name = self._generate_tree_name()
        self.filename = self.tree_name.lower().replace(" ", "-") + ".svg"


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


    def write_file(self, directory=""):
        """
        Write SVG to filename.
        """
        if directory:
            if directory[-1] != "/":
                directory += "/"
        
        full_path = directory + self.filename

        self.svg_img.saveas(full_path, pretty=True, indent=2)


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
            self.bark_colour_name = "Brown"
        else:
            colour = random.choice(colours.GRAYS)
            self.bark_colour = svgwrite.rgb(*colour)
            self.bark_colour_name = random.choice(["Silver", "Gray", "Grey"])
        
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
            self.foliage_colour_name = "Green"
        elif 0.80 < colour_selector <= 0.90:
            colour = random.choice(colours.ORNAMENTAL)
            self.foliage_colour = svgwrite.rgb(*colour)
            self.foliage_colour_name = "Ornamental"
        else:
            colour = random.choice(colours.FLOWERING)
            self.foliage_colour = svgwrite.rgb(*colour)
            self.foliage_colour_name = "Flowering"
        
        print(f"Selected {self.foliage_colour_name} leaves with colour {colour}")
    
    
    def _generate_tree_name(self) -> str:
        """
        In order to get variety in the names, there will be a lot of options for modifiers with only 1-3 of them chosen for each tree.
        A final tree name will be something like: ModiferA ModifierB Species, e.g. Eastern Swamp Chestnut or Russian Flowering Aspen
        Modifier types that can be chosen with some examples:
        Direction - Northern, Western
        Region - American, European, Mediterranean
        Misc - Common, Devil's
        Biome - Swamp, Mountain, Coastal
        Colour - Bark or Foliage colour non-standard
        biome and colour are exclusive modifiers, they will not be returned together

        All trees will have a species
        Species - Hemlock, Ash, Maple, Cherry

        Ordering of modifiers is
        Direction Region Misc Biome Colour Species
        """
        tree_name = []

        num_modifiers = 0
        mod_selector = random.random()
        if mod_selector <= 0.60:  # 1 modifier
            if self.foliage_colour_name != "Green" and random.random() > 0.7:
                tree_name.append(self.foliage_colour_name)
            elif self.bark_colour_name != "Brown" and random.random() > 0.7:
                tree_name.append(self.bark_colour_name)
            else:
                tree_name.append(random.choice(names.ALL_MODIFIERS))
        elif 0.60 < mod_selector <= 1.0:  # 2 modifiers
            # Select a geographic modifier
            geo_selector = random.random()
            if geo_selector <= 0.30:
                tree_name.append(random.choice(names.DIRECTION))
            elif 0.30 < geo_selector <= 0.90:
                tree_name.append(random.choice(names.REGION))
            else:
                tree_name.append(random.choice(names.MISC))
            
            # Select a biome or colour modifier
            if random.random() <= 0.5:
                tree_name.append(random.choice(names.BIOME))
            else:
                if self.foliage_colour_name != "Green" and random.random() > 0.7:
                    tree_name.append(self.foliage_colour_name)
                elif self.bark_colour_name != "Brown" and random.random() > 0.7:
                    tree_name.append(self.bark_colour_name)
                else:
                    tree_name.append(random.choice(names.COLOUR))
        
        # Finally append the species
        tree_name.append(random.choice(names.SPECIES))
        return " ".join(tree_name)


if __name__ == "__main__":
    entry = EntryWriter()
    entry.generate_svg()
    entry.write_file()
