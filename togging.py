import os
from functools import wraps
from datetime import datetime

if os.path.exists('log.txt'):
    os.remove('log.txt')


def get_time():
    return datetime.now().strftime('%Y:%m:%d_%H:%M:%S - ')


def logging(func):
    """This decorator logs the call time and parameters of a function
    as well as indicating if the function was successful"""
    func.__q 
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(get_time() + f"Function: {func.__qualname__} succeeded with args: {*args, {**kwargs}}\n") 
        except Exception as e:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(get_time() + f"Function: {func.__qualname__} failed with args: {*args, {**kwargs}} and error: {e.__repr__()}\n")
            raise e
        return result
    return wrapper


def type_checker(func):
    """Checks the types of the arguments and return value and throws an error if there's a mismatch.
    NOTE: if you decorate a method with this decorator, then you need to call the object reference "self" """

    @wraps(func)
    def wrapper(*args, **kwargs):
        varnames = list(func.__code__.co_varnames)
        type_dict = func.__annotations__

        if varnames[0] == 'self':
            real_args = args[1:]
            varnames = varnames[1:]
        else:
            real_args = args

        for param, val in kwargs.items():
            t = type(val)

            try:
                s = type_dict[param]
            except KeyError:
                s = t

            if s != t:
                raise TypeError(f'Expected type {s} for argument {param} but got type {t}')
            varnames.remove(param)

        for param, val in zip(varnames, real_args):
            t = type(val)

            try:
                s = type_dict[param]
            except KeyError:
                s = t

            if s != t:
                raise TypeError(f'Expected type {s} for argument {param} but got type {t}')

        result = func(*args, **kwargs)

        t = type(result)
        try:
            r = type_dict['return']
        except KeyError:
            r = t

        if r != t:
            raise TypeError(f'Expected return type {r}  but got type {t}')
        return result
    return wrapper


def togging(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, logging(type_checker(val)))
    return cls