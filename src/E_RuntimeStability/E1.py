from __future__ import annotations
from functools import wraps
import numpy as np

def positive(_func=None, *, idx=None):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if idx is None:

                for a in args:
                    if isinstance(a, (int, float, np.number)) and a <= 0:
                        raise Exception("Sorry, not positive")
                    
                for v in kwargs.values():
                    if isinstance(v, (int, float, np.number)) and v <= 0:
                        raise Exception("Sorry, not positive")
                    
            else:
                if not (0 <= idx < len(args)):
                    raise Exception("Index out of bounds")
                
                val = args[idx]

                if isinstance(val, (int, float, np.number)) and val <= 0:
                    raise Exception("Sorry, not positive")

            return func(*args, **kwargs)

        return wrapper

    if isinstance(_func, int):
        return positive(idx=_func)

    if callable(_func):
        return decorator(_func)

    return decorator


if __name__ == "__main__":
    @positive(0)
    def testfun(a, b, c):
        return a, b, c

    print("OK:", testfun(1, 1, 2)) 
    print("OK:", testfun(-1, 1, 2)) 


