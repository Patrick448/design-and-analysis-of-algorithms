from util import read_file
import pydot

class Graph:
    edges = []
    nodes = []

    def __init__(self, nodes=None, edges=None, file_path=None, directed=False):
        self.edges = edges
        self.nodes = nodes
        self.directed = directed

        if self.edges is None and self.nodes is None and file_path is not None:
            self.create_from_file(file_path)

    def to_pydot(self, engine="dot"):
        graph_type = "digraph" if self.directed else "graph"
        graph = pydot.Dot(graph_type=graph_type, rankdir="LR", concentrate=True, layout=engine)
        for node in self.nodes:
            graph.add_node(pydot.Node(str(node)))
        for edge in self.edges:
            graph.add_edge(pydot.Edge(str(edge[0]), str(edge[1])))
        return graph

    def create_from_file(self, file_path):
        content = read_file(file_path)
        split_content = content.split('#')

        graph_type = split_content[0].strip('\n')
        nodes_str = split_content[1].strip('\n')
        edges_str = split_content[2].strip('\n')

        self.edges = eval(edges_str)
        self.nodes = eval(nodes_str)
        self.directed = True if graph_type.lower() == "digraph" else False

    def get_adjacency_list(self):
        adjacency_list = {node: [] for node in self.nodes}
        for edge in self.edges:
            adjacency_list[edge[0]].append(edge[1])

            #if not self.directed:
            adjacency_list[edge[1]].append(edge[0])

        return adjacency_list

    def dfs_compute_tdc(self, node):
        stack = []
        visited = {node: False for node in self.nodes}
        stack.append(node)
        adjacency_list = self.get_adjacency_list()

        while len(stack) > 0:
            top = stack[len(stack) - 1]
            visited[top] = True
            all_children_visited = True

            for node in adjacency_list[top]:
                if not visited[node]:
                    stack.append(node)
                    all_children_visited = False

            if all_children_visited:
                stack.pop()

        return [node for node in self.nodes if visited[node]]

    def check_connected(self):
        dfs = self.dfs_compute_tdc(self.nodes[0])
        set_dfs = set(dfs)
        set_nodes = set(self.nodes)

        return True if set_dfs == set_nodes else False


