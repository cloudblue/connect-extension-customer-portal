from anvil import alert, server

from .auth import handle_auth_error


DEBUG = None
BASE_URL = None


def handle_server_response(show_alert=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if response.get('success'):
                return response.get('result')
            elif show_alert:
                alert(f"Error during fetching data from server. Error: {response['error']}")
        return wrapper
    return decorator

  
@handle_auth_error
@handle_server_response()
def initiate_auth(email, recaptcha_token):
    return server.call('initiate_auth', email, recaptcha_token)


@handle_auth_error
@handle_server_response(show_alert=False)
def validate_token(email, passcode, recaptcha_token):
    return server.call('validate_token', email, passcode, recaptcha_token)
    

@handle_auth_error
@handle_server_response()
def list_products():
    return server.call('list_products')


@handle_auth_error
@handle_server_response()
def get_account():
    return server.call('get_account')


@handle_auth_error
@handle_server_response()
def get_product_actions(product_id):
    return server.call('list_product_actions', product_id)


@handle_auth_error
@handle_server_response()
def get_activation_template(subscription_id):
    return server.call('get_activation_template', subscription_id)


@handle_auth_error
@handle_server_response()
def get_action_link(product_id, subscription_id, action_id):
    return server.call('get_action_link', product_id, subscription_id, action_id)


@handle_auth_error
@handle_server_response()
def list_product_subscriptions(product_id):
    return server.call('list_product_subscriptions', product_id)


@handle_auth_error
@handle_server_response()
def get_connect_base_url():
    global BASE_URL
    if BASE_URL is None:
        BASE_URL = server.call('get_connect_base_url')
    return BASE_URL


@handle_auth_error
@handle_server_response()
def is_debug():
    global DEBUG
    if DEBUG is None:
        DEBUG = server.call('is_debug')
    return DEBUG  
