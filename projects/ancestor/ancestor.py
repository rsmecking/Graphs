from util import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for vert in ancestors:
        graph.add_vertex(vert[0])
        graph.add_vertex(vert[1])

    for vert in ancestors:
        graph.add_edge(vert[1], vert[0])

    # print(graph.dft(starting_node))

    # print(graph.vertices)

    earliest = graph.dft(starting_node)[-1]
    if earliest == starting_node:
        return -1
    else:
        return earliest