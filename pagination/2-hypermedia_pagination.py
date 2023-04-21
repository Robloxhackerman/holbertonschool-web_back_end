#!/usr/bin/env python3
"""
Implement a method named get_page that takes two
integer arguments page with default value 1 and
page_size with default value 10
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """

    :param page:
    :param page_size:
    :return:
    """

    finalSize: int = page * page_size
    starttSize: int = finalSize - page_size

    return starttSize, finalSize


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """

        :param page:
        :param page_size:
        :return:
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return pagination[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
