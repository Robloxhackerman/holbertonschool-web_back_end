#!/usr/bin/env python3
"""
aaaa
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """

    :param password:
    :return:
    """
    pass_encoded = password.encode()
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed
