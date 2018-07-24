import networkx as nx
from bokeh.io import show, output_file
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, TapTool, BoxSelectTool, ColumnDataSource, LabelSet
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes


G = nx.Graph()

defs = {'Elliston, B. 2013': 'B. Elliston, I. MacGill, and M. Diesendorf, “Least cost 100% renewable electricity scenarios in the Australian National Electricity Market,” Energy Policy, vol. 59, pp. 270–282, Aug. 2013.',
         'Garnaut, 2011a': None,
        'Isonet al., 2011': None
         }

nodes = list(defs.keys())

edges = [('Elliston, B. 2013', 'Garnaut, 2011a'),
         ('Elliston, B. 2013', 'Isonet al., 2011')]


G.add_nodes_from(nodes)

G.add_edges_from(edges)

plot = Plot(plot_width=400, plot_height=400,
            x_range=Range1d(-1.1,1.1), y_range=Range1d(-1.1,1.1))
plot.title.text = "Graph Interaction Demonstration"

graph_renderer = from_networkx(G, nx.spring_layout, scale=1)

graph_renderer.node_renderer.glyph = Circle(size=15)
graph_renderer.node_renderer.selection_glyph = Circle(size=15)
graph_renderer.node_renderer.hover_glyph = Circle(size=15)

graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
graph_renderer.edge_renderer.selection_glyph = MultiLine(line_width=5)
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_width=5)

graph_renderer.selection_policy = NodesAndLinkedEdges()
graph_renderer.inspection_policy = EdgesAndLinkedNodes()

pos = nx.spring_layout(G)
x,y=zip(*pos.values())

source = ColumnDataSource({'x':x,'y':y,'names': nodes})
labels = LabelSet(x='x', y='y', text='names', source=source)

plot.renderers.append(labels)

plot.renderers.append(graph_renderer)

output_file("interactive_graphs.html")
show(plot)