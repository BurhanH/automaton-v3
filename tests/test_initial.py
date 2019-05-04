# initial sample


def inc(x) -> int:
    return x + 1


def test() -> None:
    if not inc(4) == 5:
        raise AssertionError()
