#!/usr/bin/env python3
"""
aaaa
"""
import uuid

from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    aaaaa
    """
    pass

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """

        :param user_id:
        :return:
        """

        if user_id is None or isinstance(user_id, str) is False:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """

        :param session_id:
        :return:
        """

        if session_id is None or isinstance(session_id, str) is False:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """

        :param request:
        :return:
        """

        session_id = self.session_cookie(request)

        return User.get(self.user_id_for_session_id(session_id))
