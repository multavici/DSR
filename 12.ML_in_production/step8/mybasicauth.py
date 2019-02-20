"""Implements basic authentication decorator for Flask

See https://palladium.readthedocs.io/en/latest/user/deployment.html#authorization
"""


from functools import wraps

from flask import request, Response


access = {}


def init_access():
    with open('auth.txt') as f:
        for line in f.readlines():
            if line.strip():
                username, password = line.strip().split(':')
                access[username] = password


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return access.get(username) == password


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


init_access()
