#!/usr/bin/env python3
"""
aaaa
"""
from typing import TypeVar, List


class Auth:
    """
    aaaaaaaa
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        :param path:
        :param excluded_paths:
        :return:
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """

        :param request:
        :return:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        return None
