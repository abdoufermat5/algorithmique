import networkx as nx


graph = nx.Graph()

edgelist = [['Mannheim', 'Frankfurt', 85], ['Mannheim', 'Karlsruhe', 80], ['Erfurt', 'Wurzburg', 186],
            ['Munchen', 'Numberg', 167], ['Munchen', 'Augsburg', 84], ['Munchen', 'Kassel', 502],
            ['Numberg', 'Stuttgart', 183], ['Numberg', 'Wurzburg', 103], ['Numberg', 'Munchen', 167],
            ['Stuttgart', 'Numberg', 183], ['Augsburg', 'Munchen', 84], ['Augsburg', 'Karlsruhe', 250],
            ['Kassel', 'Munchen', 502], ['Kassel', 'Frankfurt', 173], ['Frankfurt', 'Mannheim', 85],
            ['Frankfurt', 'Wurzburg', 217], ['Frankfurt', 'Kassel', 173], ['Wurzburg', 'Numberg', 103],
            ['Wurzburg', 'Erfurt', 186], ['Wurzburg', 'Frankfurt', 217], ['Karlsruhe', 'Mannheim', 80],
            ['Karlsruhe', 'Augsburg', 250], ["Mumbai", "Delhi", 400], ["Delhi", "Kolkata", 500],
            ["Kolkata", "Bangalore", 600], ["TX", "NY", 1200], ["ALB", "NY", 800]]

for edge in edgelist:
    graph.add_edge(edge[0], edge[1], weight=edge[2])

# Now we want to find out distinct continents and their cities from this graph.
components = {}
for index, component in enumerate(nx.connected_components(graph)):
    components['con ' + str(index)] = component

print(components)
