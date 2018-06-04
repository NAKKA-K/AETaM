from flask import request
from flask import abort

# Check that the Content-Type is valid
def content_type(*dargs, **dkwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not dargs:
                raise ValueError('Not found variable of content_type function')
            if ('Content-Type' not in request.headers or
                    request.headers['Content-Type'] not in dargs):
                abort(400)
            return func(*args, **kwargs)

        return wrapper
    return decorator
