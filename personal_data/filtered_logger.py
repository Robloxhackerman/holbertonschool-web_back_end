#!/usr/bin/env python3
"""

"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    pepe = message
    for field in fields:
        pepe = re.sub(field + "=.*?" + separator,
                      field + "=" + redaction + separator, pepe)
    return pepe
