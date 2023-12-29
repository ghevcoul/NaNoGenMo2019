import * as colours from "./colours"
import * as names from "./names"
import * as random from "./random"

// Helper function to convert between degrees and radians
function degreeToRadian(angle: number): number {
  return angle * (Math.PI / 180.0)
}

class Point {
  x: number
  y: number

  constructor(x: number, y: number) {
    this.x = x
    this.y = y
  }
}

class LineSegment {
  start: Point
  end: Point

  constructor(start: Point, end: Point) {
    this.start = start
    this.end = end
  }

  length() {
    return Math.sqrt((this.end.x - this.start.x) ** 2 + (this.end.y - this.start.y) ** 2)
  }
}

export class Branch {
  line: LineSegment
  width: number
  leaf: boolean
  
  constructor(start: Point, branchLen: number, branchAngle: number, leafThresh: number) {
    const end = new Point(
      start.x + (branchLen * Math.cos(degreeToRadian(branchAngle))),
      start.y + (branchLen * Math.sin(degreeToRadian(branchAngle)))
    )
    this.line = new LineSegment(start, end)

    const width = Math.floor(this.line.length() / random.getRandomInt(6, 9))
    this.width = width >= 1 ? width : 1

    this.leaf = this.line.length() <= leafThresh
  }
}

export class FractalTree {

  private trunkLength = 150
  private minBranchMultiplier = 0.45
  private maxBranchMultiplier = 0.85
  private leafThreshold: number
  private minLength = 3
  
  private startAngle = 270
  private minAngle = -65
  private maxAngle = 65
  
  private numBranches = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]

  private startPos: Point

  branches: Branch[]
  barkColour: string  // RGB string of colour
  barkColourName: string  // Human-readable name for colour
  foliageColour: string
  foliageColourName: string
  name: string

  constructor(width: number, height: number) {
    // Place the starting point at width/2, height because the canvas
    // origin is at the top-left corner
    this.startPos = new Point(width / 2, height)
    this.leafThreshold = random.getRandomInt(5, 25)
    this.branches = new Array<Branch>()
  }

  generate() {
    this.buildTree(this.startPos, this.trunkLength, this.startAngle)
    this.selectBarkColour()
    this.selectFoliageColour()
    this.createTreeName()
  }

  // Private recursive function to build a tree
  private buildTree(start: Point, branchLen: number, branchAngle: number) {
    if (branchLen > this.minLength) {
      const branch = new Branch(start, branchLen, branchAngle, this.leafThreshold)
      this.branches.push(branch)

      const newBranches = random.getValueFromArray(this.numBranches)
      for (let i = 0; i < newBranches; i++) {
        const newLength = branchLen * random.getRandomFloat(this.minBranchMultiplier, this.maxBranchMultiplier)
        const newAngle = branchAngle + random.getRandomInt(this.minAngle, this.maxAngle)
        this.buildTree(branch.line.end, newLength, newAngle)
      }
    }
  }

  // Function to select the bark colour to use for this tree
  // 70% chance of a brown bark, 30% chance of gray/silver
  private selectBarkColour() {
    if (random.getRandomFloat(0.0, 1.0) <= 0.7) {
      this.barkColour = random.getValueFromArray(colours.BROWNS)
      this.barkColourName = "Brown"
    } else {
      this.barkColour = random.getValueFromArray(colours.GRAYS)
      this.barkColourName = random.getValueFromArray(["Silver", "Gray", "Grey"])
    }
  }

  // Function to select the foliage colour for this tree
  // 80% chance of green foliage, 10% each for ornamental or flowering
  private selectFoliageColour() {
    const colourSelector = random.getRandomFloat(0.0, 1.0)
    if (colourSelector <= 0.8) {
      this.foliageColour = random.getValueFromArray(colours.GREENS)
      this.foliageColourName = "Green"
    } else if (colourSelector <= 0.9) {
      this.foliageColour = random.getValueFromArray(colours.ORNAMENTAL)
      this.foliageColourName = "Ornamental"
    } else {
      this.foliageColour = random.getValueFromArray(colours.FLOWERING)
      this.foliageColourName = "Flowering"
    }
  }

  // In order to get variety in the names, there will be a lot of options for modifiers with only 1-3 of them chosen for each tree.
  // A final tree name will be something like: ModiferA ModifierB Species, e.g. Eastern Swamp Chestnut or Russian Flowering Aspen
  // Modifier types that can be chosen with some examples:
  // Direction - Northern, Western
  // Region - American, European, Mediterranean
  // Misc - Common, Devil's
  // Biome - Swamp, Mountain, Coastal
  // Colour - Bark or Foliage colour non-standard
  // biome and colour are exclusive modifiers, they will not be returned together

  // All trees will have a species
  // Species - Hemlock, Ash, Maple, Cherry

  // Ordering of modifiers is
  // Direction Region Misc Biome Colour Species
  private createTreeName() {
    const treeName = Array<string>()

    if (random.getRandomFloat(0.0, 1.0) <= 0.6) { // generate with 1 modifier
      if (this.foliageColourName !== "Green" && random.getRandomFloat(0.0, 1.0) > 0.7) {
        treeName.push(this.foliageColourName)
      } else if (this.barkColourName !== "Brown" && random.getRandomFloat(0.0, 1.0) > 0.7) {
        treeName.push(this.barkColourName)
      } else {
        treeName.push(random.getValueFromArray(names.ALL_MODIFIERS))
      }
    } else { // generate with 2 modifiers
      // Select a geographic modifier
      const geoSelector = random.getRandomFloat(0.0, 1.0)
      if (geoSelector <= 0.3) {
        treeName.push(random.getValueFromArray(names.DIRECTION))
      } else if (geoSelector <= 0.9) {
        treeName.push(random.getValueFromArray(names.REGION))
      } else {
        treeName.push(random.getValueFromArray(names.MISC))
      }

      // Select a biome or colour modifier
      if (random.getRandomFloat(0.0, 1.0) <= 0.5) {
        treeName.push(random.getValueFromArray(names.BIOME))
      } else {
        if (this.foliageColourName !== "Green" && random.getRandomFloat(0.0, 1.0) > 0.7) {
          treeName.push(this.foliageColourName)
        } else if (this.barkColourName !== "Brown" && random.getRandomFloat(0.0, 1.0) > 0.7) {
          treeName.push(this.barkColourName)
        } else {
          treeName.push(random.getValueFromArray(names.COLOUR))
        }
      }
    }

    // Finally append the species
    treeName.push(random.getValueFromArray(names.SPECIES))
    this.name = treeName.join(" ")
  }
}
