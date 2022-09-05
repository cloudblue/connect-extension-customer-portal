from .config import RECAPTCHA_SITE_KEY

from anvil.js.window import grecaptcha


def enforce_recaptcha(func):
    def wrapper(*args, **kwargs):
        def action(token):
            kwargs['recaptcha_token'] = token
            func(*args, **kwargs)
        
        token = grecaptcha.execute(
            RECAPTCHA_SITE_KEY,
            {'action': 'submit'},
        ).then(action)

    return wrapper
