import time
import networkx as nx

from DiGraph import DiGraph
from Ex3.GraphAlgo import GraphAlgo


# def my_to_nx(graph_x,graph: DiGraph):
#     nodes = graph.get_all_v()
#     for k, v in nodes.items():
#         graph_X.add_node(k)
#
#     for k, v in nodes.items():
#         for dest, weight in graph.all_out_edges_of_node(k).items():
#             graph_X.add_edge(k, dest, weight=weight)


if __name__ == '__main__':
    test_graph = GraphAlgo()
    test_graph.load_from_json("Graphs_on_circle/G_10_80_1.json")
    start=time.time()
    test_graph.shortest_path(1,3)
    print("Short path is: ",time.time()-start)
    start = time.time()
    test_graph.connected_component(5)
    print("component: ",time.time()-start)
    start = time.time()
    test_graph.connected_components()
    print("components is: ",time.time()-start)
    # graph_X = nx.DiGraph()
    # my_to_nx(graph_X,test_graph.get_graph())
    # start = time.time()
    # nx.shortest_path(graph_X,source=1,target=4,weight='weight')
    # print("short_path NETWORKX is: ",time.time()-start)
