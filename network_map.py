import networkx as nx
from bokeh.io import show, output_file
from bokeh.models import Plot, Range1d, MultiLine, Circle, ColumnDataSource, LabelSet, Span
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh import colors
import numpy as np
import author_space

def create_cit_map(nodes, edges, years, authors_and_nodes, best_order):

    best_order_flat = author_space.flatten_space(best_order)

    G = nx.DiGraph()

    G.add_nodes_from(nodes)

    G.add_edges_from(edges)

    plot = Plot(plot_width=800, plot_height=800, x_range=Range1d(-1.5,1.5), y_range=Range1d(-1.5,1.5))
    plot.title.text = ""

    graph_renderer = from_networkx(G, nx.spring_layout, scale=1.25)

    pos = graph_renderer.layout_provider.graph_layout
    xs,ys=zip(*pos.values())
    years = [years[name] for name in nodes]
    max_year = max(years)
    min_year = min(years)
    time = max_year - min_year
    xs = tuple([ -1 + 2 * (year - min_year)/time for year in years])

    ys_initial = tuple(np.arange(-1.25, 1.25, 2.5/len(nodes)))
    y_map = {}

    for author_list, y in zip(best_order_flat, ys_initial):
        y_map[author_list] = y

    ys = [y_map[authors_and_nodes[node]] for node in nodes]

    for name, x, y in zip(nodes, xs, ys):
        graph_renderer.layout_provider.graph_layout[name] = (x, y)

    graph_renderer.node_renderer.glyph = Circle(size=5)

    graph_renderer.edge_renderer.glyph = MultiLine(line_color=colors.named.cornflowerblue, line_alpha=0.8, line_width=2)

    graph_renderer.selection_policy = NodesAndLinkedEdges()
    graph_renderer.inspection_policy = EdgesAndLinkedNodes()

    # Vertical line
    last_pos = -1.25
    for index, group in enumerate(best_order):
        y_position = last_pos + len(group) * 2.5 / len(nodes)
        last_pos = y_position
        y_position = y_position - 0.5 * (2.5 / len(nodes))
        if index < len(best_order) - 1:
            if len(best_order[index + 1]) > 1:
                vline = Span(location=y_position, dimension='width', line_color='red', line_width=1, line_dash='dashed')
                plot.renderers.extend([vline])
        else:
            vline = Span(location=y_position, dimension='width', line_color='red', line_width=1, line_dash='dashed')
            plot.renderers.extend([vline])




    source = ColumnDataSource({'x':xs,'y':ys,'names': nodes})
    labels = LabelSet(x='x', y='y', text='names', text_font_size='8pt', source=source, level='glyph', x_offset=-50, y_offset=5)

    plot.renderers.append(labels)

    plot.renderers.append(graph_renderer)
    #plot.add_layout(labels)
    output_file("interactive_graphs.html")
    show(plot)