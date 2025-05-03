# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V')  # Type variable for vertices


class WeightedGraph(Graph[V], Generic[V]):

    def __init__(self, vertices: List[V] = []) -> None:
        super().__init__()
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]
        self._vertices: List[V] = vertices
        self._adjacency_list: List[List[WeightedEdge]] = [[] for _ in vertices]


    def add_edge_by_indices(self, source_index: int, target_index: int, weight: float) -> None:
        """
        Adds an edge to the graph using indices.
        """
        if source_index < 0 or source_index >= len(self._vertices):
            raise IndexError("Source index out of range")
        if target_index < 0 or target_index >= len(self._vertices):
            raise IndexError("Target index out of range")
        edge = WeightedEdge(self._vertices[source_index], self._vertices[target_index], weight)
        self._adjacency_list[source_index].append(edge)