from algo import buildDag, findArea
from ui.lib import Plot
from ui.visualizer import Visualizer
from ui.plot_utils import *


if __name__ == '__main__':
    visualizer = Visualizer([])
    plot = Plot()
    plot.draw()

    lines = getLineObjects(getLineSegments(plot))

    dag = buildDag(lines, visualizer)
    tr = findArea(dag.root, Point(0.5, 0.5))
    visualizer.addFigure(tr.toLines())

    plot = Plot(visualizer.getScenes())
    plot.draw()


