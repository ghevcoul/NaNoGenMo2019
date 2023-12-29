import { Branch, FractalTree } from "./fractal_tree"

export class CanvasPainter {
  private canvas: HTMLCanvasElement
  private context: CanvasRenderingContext2D
  private nameContainer: HTMLDivElement

  constructor() {
    this.nameContainer = document.getElementById("treeName") as HTMLDivElement
    let canvas = document.getElementById("treeSpace") as HTMLCanvasElement
    let context = canvas.getContext("2d")!

    context.lineCap = "round"
    context.lineJoin = "round"

    this.canvas = canvas
    this.context = context
  }

  clearCanvas() {
    this.context.clearRect(0, 0, 800, 800)
  }

  drawTree(tree: FractalTree) {
    this.nameContainer.innerText = tree.name

    for (const branch of tree.branches) {
      this.context.lineWidth = branch.width
      this.context.strokeStyle = branch.leaf ? tree.foliageColour : tree.barkColour

      this.context.beginPath()
      this.context.moveTo(branch.line.start.x, branch.line.start.y)
      this.context.lineTo(branch.line.end.x, branch.line.end.y)
      this.context.stroke()
    }
  }

  draw() {
    this.context.fillStyle = "rgb(200, 0, 0)"
    this.context.fillRect(10, 10, 50, 50)

    this.context.fillStyle = "rgba(0, 0, 200, 0.5)"
    this.context.fillRect(30, 30, 50, 50)
  }

}