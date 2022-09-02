from anvil import alert, open_form
from anvil.users import AuthenticationFailed


def handle_auth_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AuthenticationFailed as e:
            alert(f'Please login to go ahead with the operation. Error: {e.message}')
            open_form('LoginEmail')

    return wrapper
