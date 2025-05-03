# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


from __future__ import annotations
from dataclasses import dataclass
from edge import Edge


@dataclass(frozen=True, order=True, eq=True)
class WeightedEdge(Edge):
    """
    Class representing a weighted edge in a graph.
    """
    weight: float
    def reversed(self) -> WeightedEdge:
        """
        Returns a new WeightedEdge with the source and target reversed.
        """
        return WeightedEdge(self.target, self.source, self.weight)

    def __lt__(self, other: WeightedEdge) -> bool:
        """
        Compares two WeightedEdges based on their weights.
        """
        return self.weight < other.weight


    def __str__(self) -> str:
        return f"{self.__class__.__name__}(source={self.source}, target={self.target}, weight={self.weight})"
