

def euler(func, t_range, x0, num_steps=100):
    """

    :param func:
    :param t_range:
    :param x0:
    :param num_steps:
    :return:
    """
    h = (t_range[1] - t_range[0]) / num_steps

    t = [t_range[1] + i * h for i in range(num_steps + 1)]
    x = [x0]
    for i, ti in enumerate(t[1:], start=1):
        x[i] = x[i-1] + h * func(x[i], ti)

    return t, x

