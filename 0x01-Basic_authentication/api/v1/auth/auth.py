#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manage authenication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            - path(str): Url path to be checked
            - excluded_paths(List of str): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path[-1] == '/' and path in excluded_paths:
            return False
        if path[-1] != '/':
            path = path + '/'
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from a request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a User instance from information from a request object"""
        return None
