from .config import RECAPCHA_SITE_KEY

from anvil.js.window import grecaptcha


def enforce_recapcha(func):
    def wrapper(*args, **kwargs):
        def action(token):
            kwargs['recapcha_token'] = token
            func(*args, **kwargs)
        
        token = grecaptcha.execute(
            RECAPCHA_SITE_KEY,
            {'action': 'submit'},
        ).then(action)

    return wrapper
