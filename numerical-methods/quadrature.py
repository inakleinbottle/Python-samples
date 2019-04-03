
def trapezium(func, a, b, num_points=100):
    """
    Trapezium rule for computing integrals.

    :param func:
    :param a:
    :param b:
    :param num_points:
    :return:
    """

    h = (b - a) / num_points
    points = [a + i * h for i in range(num_points)]

    return  (h / 2.) * (func(a) + func(b) + 2. * sum(func(x) for x in points))