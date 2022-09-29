# Configure Recaptcha

## Using Anvil Editor

### Step 1 - Get recaptcha settings
Get your recaptcha key and secret from [Google Recaptcha](https://www.google.com/recaptcha/admin)

### Step 2 - Configure Frontend

1. Modify `client_code` -> `script` -> `config.py` to put value of recaptcha key value in place of `{recaptcha_client_key}`.
2. Modify 'Native Library' to replace `{recaptcha_client_key}` with the recaptcha key value.

### Step 3 - Configure Server

1. Open Secrets
2. Put recaptcha secret as value for the defined secret `RECAPTCHA_SECRET`.


## Using Python IDE

### Step 1 - Get recaptcha settings
Get your recaptcha key and secret from [Google Recaptcha](https://www.google.com/recaptcha/admin)

### Step 2 - Configure Frontend

1. Modify `client_code` -> `script` -> `config.py` to put value of recaptcha key value in place of `{recaptcha_client_key}`.
2. Modify `anvil.yaml` to replace `{recaptcha_client_key}` with the recaptcha key value.

### Step 3 - Configure Server

1. Open `settings` -> `config.yaml` and put value of secret `RECAPTCHA_SECRET` as recaptcha secret.

# Enable recaptcha for any server method call

```python
from .recaptcha import ensure_recaptcha

@ensure_recaptcha
def server_action(param1, param2, recaptcha_token):
    ...
```

**NOTE**: For recaptcha enabled server methods, it´s mandatory to have a parameter with name `recaptcha_token`.

# Client side code changes for invoking recaptcha enabled server methods

```python
from ..scripts.recaptcha import enforce_recaptcha
from anvil import server

@enforce_recaptcha
def continue_button_click(self, recaptcha_token, **event_args):
    param1 = ...
    param2 = ...
    return server.call('server_action', param1, param2, recaptcha_token)
    ...
```

