#!/usr/bin/env python3
"""
take a mixed list and return their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    sum a mixed list
    """

    return sum(num for num in mxd_list)
