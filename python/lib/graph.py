"""Simple implementation of an Acyclic Directed Graph"""


class Node:
    def __init__(self, key):
        self.key = key
        self.edges_to = {}
        self.edges_from = {}

    def link_to(self, node, weight=None):
        if node.key in self.edges_to:
            raise ValueError('Edge {source} -> {dest} already exists'.format(
                source=self.key, dest=node.key))
        node.edges_from.setdefault(self.key, self)
        self.edges_to[node.key] = (node, weight)


class Graph:
    def __init__(self, edges=[]):
        self.node_index = {}
        for from_key, to_key, weight in edges:
            self.add_edge(from_key, to_key, weight)

    def add_edge(self, from_key, to_key, weight):
        source = self.node_index.setdefault(from_key, Node(from_key))
        dest = self.node_index.setdefault(to_key, Node(to_key))
        source.link_to(dest, weight)

    def descendents(self, key):
        descendents = []
        node = self.node_index.get(key)
        if not node:
            return descendents
        descendents.extend(node.edges_to.keys())
        for child_key in node.edges_to.keys():
            descendents.extend(self.descendents(child_key))
        return descendents

    def ancestors(self, key):
        ancestors = []
        node = self.node_index.get(key)
        if not node:
            return ancestors
        ancestors.extend(node.edges_from.keys())
        for parent_key in node.edges_from.keys():
            ancestors.extend(self.ancestors(parent_key))
        return ancestors
