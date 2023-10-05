#!/usr/bin/env python3
"""
module to sum list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    get an input list of floats and return their sum as a float
    """
    answer = 0.0
    for num in input_list:
        answer = answer + num

    return answer
