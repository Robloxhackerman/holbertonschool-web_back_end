#!/usr/bin/env python3
"""
aaaaaa
"""
import base64
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        :param decoded_base64_authorization_header:
        :return:
        """

        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        return decoded_base64_authorization_header.split(":", 1)[0], \
            decoded_base64_authorization_header.split(":", 1)[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """

        :param user_email:
        :param user_pwd:
        :return:
        """
        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        try:
            search_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in search_users:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        auth_header = self.authorization_header(request)

        header_value = self.extract_base64_authorization_header(auth_header)
        decoded_value = self.decode_base64_authorization_header(header_value)
        user_data = self.extract_user_credentials(decoded_value)
        return self.user_object_from_credentials(user_data[0], user_data[1])
