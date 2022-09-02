from anvil import secrets, server

from .utils import handle_response, to_bool


@server.callable(require_user=True)
@handle_response
def get_connect_base_url():
    base_url = secrets.get_secret('CONNECT_BASE_URL')
    if base_url:
        return base_url
    else:
        raise Exception('There is a misconfiguration in server module. Please contact your Service Provider.')


@server.callable(require_user=True)
@handle_response
def is_debug():
    return to_bool(secrets.get_secret('DEBUG'))
