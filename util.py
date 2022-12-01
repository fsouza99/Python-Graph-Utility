def showGraphVertices(graph):
    for node in graph.vertices:
        showNode(node)
    print()
    return None

def showDirectedEdge(edge):
    if edge.w is None:
        print(f'''\n\t{edge.u.data} → {edge.v.data}''')
    else:
        print(f'''\n\t{edge.u.data} → {edge.v.data}, w = {edge.w}''')
    return None

def showUndirectedEdge(edge):
    if edge.w is None:
        print(f'''\n\t{edge.u.data} ↔ {edge.v.data}''')
    else:
        print(f'''\n\t{edge.u.data} ↔ {edge.v.data}, w = {edge.w}''')
    return None

def showUndirectedGraph(graph):
    print(f'''(u={graph.u.data}, v={graph.v.data}, w={graph.w})''')
    return None

def showNode(node):
    print('(data:', node.data, end='')
    if node.parent is not None:
        print(', parent:', node.parent.data, end='')
    if node.key is not None:
        print(f''', key: {node.key})''')
    return None




