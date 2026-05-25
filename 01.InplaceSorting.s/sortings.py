"""
Sorting algorithms
"""

from __future__ import annotations
from typing import Any
from comp_swap_container import CompSwapList
import random


def trivial_sort2(data: CompSwapList[Any]):
    """
    Sorts a container with 2 or fewer elements

    :param data: data to sort inplace
    :type data: MutableSequence[Ordered]
    """
    if len(data) <= 1:
        pass
    if len(data) > 2:
        raise ValueError("Expected at most 2 elements!")
    if data.less(1, 0):
        data.swap(0, 1)

def quick_sort(data: CompSwapList[Any], lo: int = 0, hi: int = None):
    if hi is None:
        hi = len(data) - 1
    if lo >= hi:
        return
    pivot_idx = random.randint(lo, hi)
    data.swap(pivot_idx, hi)
    i = lo
    for j in range(lo, hi):
        if data.less(j, hi):
            data.swap(i, j)
            i += 1
    data.swap(i, hi)
    quick_sort(data, lo, i - 1)
    quick_sort(data, i + 1, hi)

def selection_sort(data: CompSwapList[Any]):
    n = len(data)
    for i in range(n-1):
        mn = i
        for j in range(i+1, n):
            if data.less(j, mn):
                mn = j
        if mn != i:
            data.swap(i, mn)
