export class CanvasPainter {
  private canvas: HTMLCanvasElement
  private context: CanvasRenderingContext2D

  constructor() {
    let canvas = document.getElementById("treeSpace") as HTMLCanvasElement
    let context = canvas.getContext("2d")!

    this.canvas = canvas
    this.context = context

    this.draw()
  }

  draw() {
    this.context.fillStyle = "rgb(200, 0, 0)"
    this.context.fillRect(10, 10, 50, 50)

    this.context.fillStyle = "rgba(0, 0, 200, 0.5)"
    this.context.fillRect(30, 30, 50, 50)
  }

}