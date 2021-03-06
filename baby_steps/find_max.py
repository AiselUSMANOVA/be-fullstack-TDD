def get_max(a, b):
    """
       Compare two values and return max value.
    :param a: int
    :param b: int
    :return: max value
    """
    if a>b:
        return a
    else:
        b


def get_max_without_arguments():
    """
       Raise Error, if there is no argument.
    """
    raise TypeError("No arguments");


def get_max_with_one_argument(a):
    """
       :param a: int
       Return that value.
    """
    return a


def get_max_with_many_arguments(*args):
    """
        Return largest number among args.
    """

    max_number = float('-inf')

    for arg in args:
        if arg > max_number:
            max_number = arg

    return max_number


def get_max_with_one_or_more_arguments(first, *args):
    """
        Return largest number among first + args.
    """

    max_number = float('-inf')

    for arg in (first, *args):
        if arg > max_number:
            max_number = arg

    return max_number


def get_max_bounded(*args, low, high):
    """
        Return largest number among args bounded by low & high.
    """

    max_number = float('-inf')

    for arg in args:
        if arg > max_number and (low < arg and arg < high):
            max_number = arg

    return max_number


def make_max(*, low, high):
    """
        Return inner function object which takes at last one argument
        and return largest number amount it's arguments, but if the
        largest number is larger than the 'high' which given as required
        argument the inner function has to return it.
    """

    def inner(first, *args):
        max_number = float('-inf')

        for arg in (first, *args):
            if arg > max_number and (arg > low and arg < high):
                max_number = arg
                
        return max_number

    return inner
