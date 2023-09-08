from functools import wraps
from typing import Any
from django.http import HttpRequest


class AuthenticationDecorator:

    def __init__(self, auth_token) -> None:
        self.auth_token = auth_token


    def __call__(self, func) -> Any:
        @wraps(func)
        def decorated_func(*args, **kwargs):

            auth_header = kwargs.get('headers', {}).get('Authorization')
            if auth_header != self.auth_token:
                return {'message': 'Unauthorized'}, 401
            
            return func(*args, **kwargs)
        
        return decorated_func


auth_token = 'my_auth_token'

@AuthenticationDecorator(auth_token)
def protected_endpoint(headers):
    return {'message': 'You are authorized'}

# Usage example
request_headers = {
    'Authorization': ''
}

response = protected_endpoint(headers=request_headers)
print(response)  
