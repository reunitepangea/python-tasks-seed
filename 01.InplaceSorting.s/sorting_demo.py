#!/usr/bin/env -S python3
"""
Sortings demo
"""

from comp_swap_container import CompSwapList
import sortings
import random

if __name__ == "__main__":
    # trivial_sort2
    data: CompSwapList[int] = CompSwapList([2, 1])
    sortings.trivial_sort2(data)
    print(f"Comps: {data.comps}, Swaps: {data.swaps}")
    for n in [10, 100, 1000]:
        data = CompSwapList(random.sample(range(n), n))
        sortings.selection_sort(data)
        print(f"selection_sort n={n}: comps={data.comps}, swaps={data.swaps}")

        data = CompSwapList(random.sample(range(n), n))
        sortings.quick_sort(data)
        print(f"quick_sort     n={n}: comps={data.comps}, swaps={data.swaps}")
