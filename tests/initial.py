# initial sample


def inc(x):
    return x + 1


def test():
    if not inc(4) == 5:
        raise AssertionError()
