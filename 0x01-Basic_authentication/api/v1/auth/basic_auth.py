#!/usr/bin/env python3
"""
Auth module for the API
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Manage authenication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
            Returns the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if authorization_header is None or\
                type(authorization_header) is not str:
            return None
        elif authorization_header[0:6] != 'Basic ':
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
            Returns the decoded value of a Base64
            string base64_authorization_header
        """
        if base64_authorization_header is None or\
                type(base64_authorization_header) is not str:
            return None
        try:
            result = base64.b64decode(base64_authorization_header)\
                .decode('utf-8')
            if result:
                return result
        except Exception:
            return None
