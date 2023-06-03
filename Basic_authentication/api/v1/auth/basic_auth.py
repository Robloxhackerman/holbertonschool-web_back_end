#!/usr/bin/env python3
"""
aaaaaa
"""
import base64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    aaaaaa
    """

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """

        :param authorization_header:
        :return:
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if "Basic " not in authorization_header:
            return None

        return authorization_header.split("Basic ", 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """

        :param base64_authorization_header:
        :return:
        """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None
