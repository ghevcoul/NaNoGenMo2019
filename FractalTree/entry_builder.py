
import math
import random

import svgwrite

import colours
import names
import image_writer
from fractal_tree import FractalTree

from typing import Tuple


class EntryWriter:
    """
    Generate and write an entry into the field guide.
    """
    def __init__(self, directory: str=""):
        self.tree: FractalTree = FractalTree()
        self.bark_colour: Tuple[int, int, int] = None
        self.bark_colour_name: str = None
        self.foliage_colour: Tuple[int, int, int] = None
        self.foliage_colour_name: str = None

        self._select_bark_colour()
        self._select_foliage_colour()
        self.tree_name = self._generate_tree_name()

        if directory:
            if directory[-1] != "/":
                directory += "/"
        self.filename = directory + self.tree_name.lower().replace(" ", "-")
    

    def build_tree(self) -> None:
        print(f"Creating tree {self.tree_name}")
        self.tree.generate()
        self.tree.normalize()


    def write_image(self, format: str) -> None:
        print(f"Writing {format} image of tree")
        if format == "SVG":
            fname = self.filename + ".svg"
            writer = image_writer.SVGWriter(self.tree, fname, self.bark_colour, self.foliage_colour)
            writer.write()
        elif format == "PNG":
            fname = self.filename + ".png"
            writer = image_writer.PNGWriter(self.tree, fname, self.bark_colour, self.foliage_colour)
            writer.write()
        else:
            raise NotImplementedError(f"Unknown format {format}")


    def _select_bark_colour(self) -> None:
        """
        Chooses the colour of the trunk of the tree. Saves the colour to the class as an RGB and a string naming the colour.

        70% chance of choosing a brown trunk, 30% chance of choosing a gray/silver
        """
        colour_selector = random.random()
        if colour_selector <= 0.70:
            self.bark_colour = random.choice(colours.BROWNS)
            self.bark_colour_name = "Brown"
        else:
            self.bark_colour = random.choice(colours.GRAYS)
            self.bark_colour_name = random.choice(["Silver", "Gray", "Grey"])
    

    def _select_foliage_colour(self) -> None:
        """
        Chooses the colour of the foliage for the tree. Saves the colour to the class as an RGB and a string naming the colour.

        80% chance of choosing green leaves, 10% chance each of choosing ornamental or flowering
        """
        colour_selector = random.random()
        if colour_selector <= 0.80:
            self.foliage_colour = random.choice(colours.GREENS)
            self.foliage_colour_name = "Green"
        elif 0.80 < colour_selector <= 0.90:
            self.foliage_colour = random.choice(colours.ORNAMENTAL)
            self.foliage_colour_name = "Ornamental"
        else:
            self.foliage_colour = random.choice(colours.FLOWERING)
            self.foliage_colour_name = "Flowering"
    
    
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
    for _ in range(25):
        entry = EntryWriter("examples/")
        entry.build_tree()
        entry.write_image("PNG")
