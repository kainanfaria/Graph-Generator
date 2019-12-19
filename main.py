import Generator

print(" --------------------------------------------------------------------------\n"
      "|Graph generator:                                                          |\n"
      "|for connected graphs type it in Type of graph, conexo                     |\n"
      "|for triangular graphs type it in Type of graph, triangular                |\n"
      "|for perfect graphs type it in Type of graph, perfeito(Not implemented)    |\n"
      " --------------------------------------------------------------------------")

typeGraph = input("Type of graph: ").upper()
if typeGraph == "CONEXO":

      vertex_number = int(input("Number of vertex: "))
      print("Edges number should be >= of verter number")
      edges_number = int(input("Number of edges: "))
      graph_name = input("Graph name: ")
      graph = Generator.graph(typeGraph, vertex_number, edges_number)
      graph.edge_generator()
      graph.save_graph(graph_name)

elif typeGraph == "TRIANGULAR":

      print("Vertex number should be >= 3")
      vertex_number = int(input("Number of vertex: "))
      graph_name = input("Graph name: ")
      graph = Generator.graph(typeGraph, vertex_number, 0)
      graph.edge_generator()
      graph.save_graph(graph_name)

elif typeGraph == "RANDOM":

      vertex_number = int(input("Number of vertex: "))
      print("Edges number should be >= of verter number")
      edges_number = int(input("Number of edges: "))
      graph_name = input("Graph name: ")
      graph = Generator.graph(typeGraph, vertex_number, edges_number)
      graph.edge_generator()
      graph.save_graph(graph_name)