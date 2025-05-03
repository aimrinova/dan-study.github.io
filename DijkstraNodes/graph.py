# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


from typing import TypeVar, Generic, List, Dict
from edge import Edge

V = TypeVar('V')  # Type variable for vertices


class Graph(Generic[V]):
    """
    Class representing a graph using an adjacency list.
    """
    def __init__(self) -> None:
        self.adjacency_list: Dict[V, List[Edge]] = {}
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]


    @property
    def vertex_count(self) -> int:
        """
        Returns the number of vertices in the graph.
        """
        return len(self._vertices)



    def add_edge(self, source: V, target: V, weight: float) -> None:
        """
        Adds an edge to the graph.
        """
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        if target not in self.adjacency_list:
            self.adjacency_list[target] = []
        edge = Edge(source, target, weight)
        self.adjacency_list[source].append(edge)

    def get_edges(self, vertex: V) -> List[Edge]:
        """
        Returns the edges connected to a vertex.
        """
        return self.adjacency_list.get(vertex, [])