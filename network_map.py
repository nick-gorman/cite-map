import networkx as nx
from bokeh.io import show, output_file
from bokeh.models import Plot, Range1d, MultiLine, Circle, ColumnDataSource, LabelSet
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes


def create_cit_map(nodes, edges):

    G = nx.DiGraph()

    G.add_nodes_from(nodes)

    G.add_edges_from(edges)

    plot = Plot(plot_width=800, plot_height=800, x_range=Range1d(-1.1,1.1), y_range=Range1d(-1.1,1.1))
    plot.title.text = ""

    graph_renderer = from_networkx(G, nx.kamada_kawai_layout, scale=1)

    graph_renderer.node_renderer.glyph = Circle(size=15)
    graph_renderer.node_renderer.selection_glyph = Circle(size=15)
    graph_renderer.node_renderer.hover_glyph = Circle(size=15)

    graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
    graph_renderer.edge_renderer.selection_glyph = MultiLine(line_width=5)
    graph_renderer.edge_renderer.hover_glyph = MultiLine(line_width=5)

    graph_renderer.selection_policy = NodesAndLinkedEdges()
    graph_renderer.inspection_policy = EdgesAndLinkedNodes()

    pos = graph_renderer.layout_provider.graph_layout
    x,y=zip(*pos.values())
    source = ColumnDataSource({'x':x,'y':y,'names': nodes})
    labels = LabelSet(x='x', y='y', text='names', source=source, level='glyph', x_offset=5, y_offset=5)

    plot.renderers.append(labels)

    plot.renderers.append(graph_renderer)
    #plot.add_layout(labels)
    output_file("interactive_graphs.html")
    show(plot)