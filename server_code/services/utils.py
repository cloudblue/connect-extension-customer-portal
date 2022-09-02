from functools import wraps


def handle_response(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            return {
                'success': True,
                'result': func(*args, **kwargs),
            }
        except Exception as e:
            error = str(e)
            print(error)
            return {
                'success': False,
                'error': error,
            }

    return wrap


def to_bool(value: str):
    return value and value.lower() in ['true', 'yes']
