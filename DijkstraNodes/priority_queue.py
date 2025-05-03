# filename: future_addonNotes/debugging_pre-post.py
# -*- coding: utf-8 -*-
# author: Daniel Schubert
# date: 2025-05-03


from typing import TypeVar, Generic, List, Dict
from heapq import heappush, heappop


T = TypeVar('T')  # Type variable for the items in the priority queue


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        """
        Initializes an empty priority queue.
        """
        self._elements: List[T] = []        # Cointtainer for the elements in the priority queue
        self._entry_finder: Dict[T, int] = {}

    @property
    def is_empty(self) -> bool:
        """
        Returns True if the priority queue is empty, False otherwise.
        """
        return not self._elements


    def push(self, item: T, priority: int) -> None:
        """
        Adds an item to the priority queue with the given priority.
        """
        heappush(self._elements, (priority, item))
        self._entry_finder[item] = priority


    def pop(self) -> T:
        """
        Removes and returns the item with the highest priority (lowest value).
        """
        while self._elements:
            priority, item = heappop(self._elements)
            if item in self._entry_finder:
                del self._entry_finder[item]
                return item
        raise KeyError("pop from an empty priority queue")


    def __rep__(self) -> str:
        """
        Returns a string representation of the priority queue.
        """
        return f"PriorityQueue({self._elements})"
