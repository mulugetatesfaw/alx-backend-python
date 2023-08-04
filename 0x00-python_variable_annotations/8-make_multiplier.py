#!/usr/bin/env python3
"""
Complex types functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float here
    """
    def multiplies(n: float):
        """
        multiply two number here
        """
        return n * multiplier
    return multiplies
