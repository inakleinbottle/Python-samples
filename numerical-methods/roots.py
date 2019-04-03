



def newton(func, x0, *, tol=1e-10, max_iterations=2 << 10):
    """
    Newton's method for root finding.

    :param func:
    :param x0:
    :param tol:
    :param max_iterations:
    :return:
    """
    try:
        f, fp = func
    except ValueError:
        raise Exception('Expected list of functions')

    x = x0
    old = x0 + 50
    i = 0

    while abs(old - x) >= tol:
        i += 1
        if i == max_iterations:
            raise Exception(f'Failed to converge after {max_iterations} iterations')

        old = x
        x = x - f(x) / fp(x)

    return x


def secant(func, x0, x1, *, tol=1e-10, max_iterations=2 << 10):
    """
    Secant method for root finding.

    :param func:
    :param x0:
    :param x1:
    :param tol:
    :param max_iterations:
    :return:
    """
    xi, xii = x0, x1
    i = 0

    while abs(xii - xi) >= tol:
        i += 1
        if i == max_iterations:
            raise Exception(f'Failed to converge after {max_iterations} iterations')

        t = xii
        xii = xii - func(xii) * (xii - xi) / (func(xii) - func(xi))
        xi = t

    return xii
