from functools import wraps


def singleton(cls):
    """
    Simple singleton pattern
    :param cls:
    :return:
    """
    instance = { }

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance
