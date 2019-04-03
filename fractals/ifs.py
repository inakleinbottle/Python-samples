





class IFS:
    """
    Iterated function system.
    """

    def __init__(self, *functions):
        self.functions = functions

    def __call__(self, points):
        return [m(pt) for pt in points for m in self.functions]

    def generate_steps(self, *initial_points, max_iterations=100_000):
        points = list(initial_points)
        if not points:
            raise ValueError('Expecting initial points')
        for _ in range(max_iterations):
            points = self(points)
            yield points




class Similarity:

    def __init__(self, function, ratio=None):
        self.function = function
        self.ratio = ratio

    def __call__(self, point):
        return self.function(point)


class SimilarityList(IFS):

    def get_simvalue(self):
        

