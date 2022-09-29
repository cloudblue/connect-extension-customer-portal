# Server side utilities

## @handle_response
This decorator is used to automatically convert the response of
a server method in a specific JSON format as specified below:

```json
{
  "success": true,
  "result": "success result from server method",
  "error": "Error from server method as raised exception"
}
```

***Usage example:***

```python
from anvil import server
from .utils import handle_response


@handle_response
def get_account():
    account = server.session['account']
    
    if account:
        return account
    else:
        raise Exception('Unable to fetch account information.')
```

***Note:*** User this decorator with `@handle_server_response`
decorator at client side code.

# Client side utilities

## @handle_server_response

This decorator is used on client side code to handle response from server methods decorated with `@handle_response`.
On error, this will show the alert using `anvil.alert()` method by default.
This behaviour can be changed by passing the parameter `show_alert=False`.

***Usage example:***

```python
from anvil import server
from ..scripts.client import handle_server_response


@handle_server_response()
def initiate_auth(email, recaptcha_token):
    return server.call('initiate_auth', email, recaptcha_token)
```

## @handle_auth_error

This decorator is used to automatically handle auth errors for
calling server methods those should be secured with authentication.

***Usage example:***

```python
from anvil import server
from .auth import handle_auth_error
from ..scripts.client import handle_server_response


@handle_auth_error
@handle_server_response()
def initiate_auth(email, recaptcha_token):
    return server.call('initiate_auth', email, recaptcha_token)
```