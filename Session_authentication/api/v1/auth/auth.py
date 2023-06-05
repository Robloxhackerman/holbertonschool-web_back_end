#!/usr/bin/env python3
"""
aaaa
"""
from os import getenv
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
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        return None

    def session_cookie(self, request=None):
        """ Returns cookie value from a request """
        if request is None:
            return None

        return request.cookies.get(getenv('SESSION_NAME'))
