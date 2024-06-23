from django.db import models

class Percentile(models.Aggregate):
    arity = 1
    function = "percentile_cont"
    template = "%(function)s(%(percentile)s) WITHIN GROUP (ORDER BY %(expressions)s)"
    name = "Percentile"

    def __init__(self, percentile, expressions, **extra):
        super().__init__(expressions, percentile=percentile, **extra)