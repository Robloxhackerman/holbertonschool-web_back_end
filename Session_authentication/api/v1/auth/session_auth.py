#!/usr/bin/env python3
"""
aaaa
"""
import uuid

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    aaaaa
    """
    pass

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for user_id """

        if user_id is None or isinstance(user_id, str) is False:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id