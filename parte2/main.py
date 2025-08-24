import pydot

from parte2.graph import Graph
from parte2.util import read_file

def main():
    graph = Graph(file_path='input1.txt')
    print(graph.dot_graph())
    (pydot_output,) = pydot.graph_from_dot_data(graph.dot_graph())
    pydot_output.write_png('graph.png')

    graph.dfs_compute_tdc('x1')

main()
