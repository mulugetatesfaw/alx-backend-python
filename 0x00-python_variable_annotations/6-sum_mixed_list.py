#!/usr/bin/env python3
"""
Complex types  mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return a sum of all numbers inside a list
    """
    return sum(mxd_lst)
