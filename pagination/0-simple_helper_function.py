#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """

    :param page:
    :param page_size:
    :return:
    """

    finalSize: int = page * page_size
    starttSize: int = finalSize - page_size

    return (starttSize, finalSize)