def decorator(cls):
    class Wrapper:
        def __init__(self, base_obj, *args, **kwargs):
            self.base_obj = base_obj

        def __lt__(self, other):
            if self.base_obj.period == other.base_obj.period:
                return self.base_obj.index < other.base_obj.index
            else:
                return self.base_obj.period < other.base_obj.period


@decorator
class RMTaskWrapper:
    def __init__(self, task):
        self.task = task
