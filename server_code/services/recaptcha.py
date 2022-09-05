from functools import wraps

from anvil import http, secrets


def __get_param_value(param_name, func, args, kwargs):
    param_value = kwargs.get(param_name)

    if not param_value:
        var_names = func.__code__.co_varnames
        position = 0
        for var_name in var_names:
            if var_name in ['args', 'kwargs']:
                continue
            elif var_name != param_name:
                position += 1
            else:
                break

        if position < len(args):
            param_value = args[position]

    return param_value


def ensure_recaptcha(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        recaptcha_token = __get_param_value('recaptcha_token', func, args, kwargs)
        recaptcha_secret = secrets.get_secret('RECAPTCHA_SECRET')
        response = http.request(    
            url=f'https://www.google.com/recaptcha/api/siteverify?secret={recaptcha_secret}&response={recaptcha_token}',
            method='POST',
            json=True,
        )
        if response and 'success' in response and response['success']:
            return func(*args, **kwargs)
        else:
            raise Exception('Failed recaptcha validation.')

    return wrap

