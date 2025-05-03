# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03

from __future__ import annotations
from typing import Any, Optional, TypeVar, cast, ParamSpec, List, Dict
from collections.abc import Callable
from dataclasses import dataclass, field
from mst import WeightedGraph, print_weighted_graph
from weighted_graph import WeightedGraph as WGraph
from weighted_edge import WeightedEdge as WEdge
from priority_queue import PriorityQueue


V = TypeVar('V') # Type variable for vertices

@dataclass
class DijkstraNode:
    """
    Class representing a node in the Dijkstra algorithm.
    """
    vertex: V
    distance: float = field(default=float('inf'))
    previous: Optional[DijkstraNode] = field(default=None)

    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool:
        return self.vertex == other.vertex and self.distance == other.distance

    def __repr__(self) -> str:
        return f"DijkstraNode(vertex={self.vertex}, distance={self.distance})"