# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


from typing import TypeVar, Generic, List, Dict
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue
from mst import MST, PrimMST, KruskalMST


V = TypeVar('V')


WeightedPath = List[WeightedEdge]    # Alias for path
def total_weight(path: WeightedPath) -> float:
    """
    Calculate the total weight of a path.
    """
    return sum(edge.weight for edge in path)
