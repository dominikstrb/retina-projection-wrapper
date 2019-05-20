import matlab


def np2mat_slow(arr):
    """ Convert a np.array to matlab.double
    Args:
        arr: np.array

    Returns: matlab.double array

    """

    return matlab.double(arr.tolist())


def np2mat(arr):
    """ Convert a np.array to matlab.double.

    This function works only with the fix proposed in https://stackoverflow.com/a/45290997

        Args:
            arr: np.array

        Returns: matlab.double array

    """
    return matlab.double(arr)


if __name__ == "__main__":
    import timeit

    setup = (
        "import numpy as np; from __main__ import np2mat, np2mat_slow; x = np.random.randn(512, 512)"
    )

    print(timeit.timeit("mat = np2mat(x)", setup=setup, number=100))

    print(timeit.timeit("mat = np2mat_slow(x)", setup=setup, number=100))
