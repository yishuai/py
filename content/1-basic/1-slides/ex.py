from operator import floordiv, mod
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(123, 10)
    >>> quotient
    12
    >>> remainder
    3
    """
    return floordiv(n, d), mod(n, d)