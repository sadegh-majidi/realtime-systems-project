def decorator(cls):
    class Wrapper:
        def __init__(self, base_obj, *args, **kwargs):
            self.base_obj = base_obj

        def __lt__(self, other):
            return self.base_obj.arrival < other.base_obj.arrival


@decorator
class FCFSTaskWrapper:
    def __init__(self, task):
        self.task = task
