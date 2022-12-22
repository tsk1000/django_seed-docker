

from django.db import transaction


@transaction.atomic
def exception(func):
    """exception wrapper"""
    def wrapper(*args, **kwargs):
        try:
            with transaction.atomic():
                fun = func(*args, **kwargs)
                return fun
        except Exception as e:
            raise

    return wrapper
