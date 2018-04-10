"""Miscellaneous utility functions.
"""


def add_callbacks(pre_cbk, post_cbk):
    """Decorator to wrap methods for pre and post callbacks, e.g. for monitoring and analysis.

    The object which method is wrapped must have implemented functions named pre_cbk and post_cbk if they are not
    None.

    :param str pre_cbk:
        Name of the method which is called before the wrapped function. The method signature should be
        pre_cbk(self, func, *args, **kwargs), where func is the wrapped function and all arguments and keyword
        arguments are the ones passed to func.
    :param str post_cbk:
        Name of the method which is called after the wrapped function. Any results of the wrapped function are
        forwarded to the callback. The method signature should be pre_cbk(self, result, func, *args, **kwargs),
        where result is the value returned by func(*args, **kwargs), func is the wrapped function and all arguments
        and keyword arguments are the ones passed to func.
    """
    def decorate(func):
        def call(*args, **kwargs):
            # args[0] is the instance of the object, i.e. self.
            if pre_cbk is not None:
                pre_method = getattr(args[0], pre_cbk)
                pre_method(func, *args, **kwargs)
            result = func(*args, **kwargs)
            if post_cbk is not None:
                post_method = getattr(args[0], post_cbk)
                post_method(result, func, *args, **kwargs)
            return result
        return call
    return decorate
