"""
Unit tests for 00.Demo
"""

import random
import pytest
from comp_swap_container import CompSwapList
import sortings


@pytest.fixture(scope="module")
def fatal_array():
    """
    Create a shuffled array of 1000 elements with fixed seed
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)


def test_trivial_sort2():
    """
    Test trivial sorting of a 2-element array
    """
    original = [2, 1]
    a2: CompSwapList[int] = CompSwapList(original)
    sortings.trivial_sort2(a2)
    assert list(a2) == sorted(original)


def test_selection_sort_empty():
    a2: CompSwapList[int] = CompSwapList([])
    sortings.selection_sort(a2)
    assert list(a2) ==[]

def test_selection_sort_one():
    a2: CompSwapList[int] = CompSwapList([1])
    sortings.selection_sort(a2)
    assert list(a2) == [1]

def test_selection_sort_two_sorted():
    a2: CompSwapList[int] = CompSwapList([1, 2])
    sortings.selection_sort(a2)
    assert list(a2) == [1, 2]

def test_selection_sort_two_unsorted():
    a2: CompSwapList[int] = CompSwapList([2, 1])
    sortings.selection_sort(a2)
    assert list(a2) == [1, 2]

def test_selection_sort_doubelements_diff():
    a2: CompSwapList[int] = CompSwapList([3, 6, 7, 3, 3, 8, 5, 3, 1, 2])
    sortings.selection_sort(a2)
    assert list(a2) == [1, 2, 3, 3, 3, 3, 5, 6, 7, 8]

def test_selection_sort_doubelements_same():
    a2: CompSwapList[int] = CompSwapList([6, 6, 6])
    sortings.selection_sort(a2)
    assert list(a2) == [6, 6, 6]

def test_selection_sort_fatal_array(fatal_array):
    fatal_array_copy = CompSwapList(fatal_array)
    sortings.selection_sort(fatal_array_copy)
    assert sorted(fatal_array) == list(fatal_array_copy)

def test_quick_sort_empty():
    a2: CompSwapList[int] = CompSwapList([])
    sortings.quick_sort(a2)
    assert list(a2) == []

def test_quick_sort_one():
    a2: CompSwapList[int] = CompSwapList([1])
    sortings.quick_sort(a2)
    assert list(a2) == [1]

def test_quick_sort_two_sorted():
    a2: CompSwapList[int] = CompSwapList([1, 2])
    sortings.quick_sort(a2)
    assert list(a2) == [1, 2]

def test_quick_sort_two_unsorted():
    a2: CompSwapList[int] = CompSwapList([2, 1])
    sortings.quick_sort(a2)
    assert list(a2) == [1, 2]

def test_quick_sort_doubelements_diff():
    a2: CompSwapList[int] = CompSwapList([3, 6, 7, 3, 3, 8, 5, 3, 1, 2])
    sortings.quick_sort(a2)
    assert list(a2) == [1, 2, 3, 3, 3, 3, 5, 6, 7, 8]

def test_quick_sort_doubelements_same():
    a2: CompSwapList[int] = CompSwapList([6, 6, 6])
    sortings.quick_sort(a2)
    assert list(a2) == [6, 6, 6]

def test_quick_sort_fatal_array(fatal_array):
    fatal_array_copy = CompSwapList(fatal_array)
    sortings.quick_sort(fatal_array_copy)
    assert sorted(fatal_array) == list(fatal_array_copy)
