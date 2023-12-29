import { CanvasPainter } from "./canvas_painter"
import { FractalTree } from "./fractal_tree"

const button = document.getElementById("generateButton")
button?.addEventListener("click", createFieldGuideEntry)

function createFieldGuideEntry() {
  const painter = new CanvasPainter()
  painter.clearCanvas()
  const tree = new FractalTree(800, 800)
  tree.generate()
  painter.drawTree(tree)
}

createFieldGuideEntry()
