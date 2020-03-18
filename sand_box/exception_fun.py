"""A module for demonstrating exceptions.

Use common or existing exceptions when possible, i.e.:

IndexError
KeyError
ValueError
TypeError
etc.

Avoid protecting against TypeErrors.  It is against the grain of Python.
"""

import sys


def convert(value):
    """Convert to an integer.  Okay."""
    try:
        the_int = int(value)
    except ValueError:
        the_int = -1
    return the_int


def another_convert(value):
    """Convert to an integer.  Better."""
    the_int = -1
    try:
        the_int = int(value)
    except (ValueError, TypeError):
        pass
    return the_int


def yet_another_convert(value):
    """Convert to an integer. Better yet."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return -1


def informative_convert(value):
    """Convert to an integer.  Prints a very helpful error message! """
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print("Conversion error: { }".format(str(e)), file=sys.stderr)
        return -1

