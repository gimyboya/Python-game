# some utils functions

import threading
from functools import wraps

def delay(delay: object = 0.) -> object:
    """
    Decorator delaying the execution of a function for a while.
    :rtype: object
    """
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap