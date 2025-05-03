# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True, order=True, eq=True)
class Edge:
    """
    Class representing an edge in a graph.
    """
    source: int     # The source vertex of the edge
    target: int     # The target vertex of the edge
    weight: float   # The weight of the edge

    def reverse(self) -> Edge:
        """
        Returns a new Edge with the source and target reversed.
        """
        return Edge(self.target, self.source, self.weight)

    def __repr__(self) -> str:
        return f"Edge(source={self.source}, target={self.target}, weight={self.weight})"