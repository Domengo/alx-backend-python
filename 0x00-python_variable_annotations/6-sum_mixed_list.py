#!/usr/bin/env python3

""" a type-annotated function sum_mixed_list that
takes a list mxd_lst of integers and floats and 
returns their sum as a float"""
from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    '''return sum mxd_lst'''
    return sum(mxd_lst)