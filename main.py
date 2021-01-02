from algo import buildDag, findArea
from ui.lib import Plot
from ui.visualizer import Visualizer
from ui.plot_utils import *
from polygons import *

if __name__ == '__main__':
    visualizer = Visualizer([])

    #lines = getLineObjects(getLineSegments(plot))
    lines = pol1

    dag = buildDag(lines, visualizer)

    test_point1 = Point(0.5, 0.5)
    test_point2 = Point(0.3, 0.7)
    tr1 = findArea(dag.root, test_point1)
    tr2 = findArea(dag.root, test_point2)
    visualizer.addDagWithResult(dag, tr1, test_point1)
    visualizer.addDagWithResult(dag, tr2, test_point2)

    plot = Plot(visualizer.getScenes())
    plot.draw()


