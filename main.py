from algo import buildDag, findArea
from ui.lib import Plot
from ui.visualizer import Visualizer
from ui.plot_utils import *
from polygons import *

if __name__ == '__main__':
    visualizer = Visualizer([])
    plot = Plot()
    plot.draw()

    lines1 = getLineObjects(getLineSegments(plot))
    #lines = pol2

    dag = buildDag(lines1, visualizer)

    test_point1 = Point(0.5, 0.5)
    tr1 = findArea(dag.root, test_point1)
    visualizer.addDagWithResult(dag, tr1, test_point1)

    plot = Plot(visualizer.getScenes())
    plot.draw()


