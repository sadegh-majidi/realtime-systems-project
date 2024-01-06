class FCFSTaskWrapper:
    def __init__(self, task):
        self.task = task

    def __getattr__(self, attr):
        return getattr(self.task, attr)

    def __lt__(self, other):
        if self.task.arrival == other.task.arrival:
            return self.task.index < other.task.index
        return self.task.arrival < other.task.arrival


class sBEETTaskWrapper:
    def __init__(self, task):
        self.task = task

    def __getattr__(self, attr):
        return getattr(self.task, attr)

    def __setattr__(self, name, value):
        if name == 'task':
            super().__setattr__(name, value)
        else:
            setattr(self.task, name, value)

    def __lt__(self, other):
        if self.task.arrival == other.task.arrival:
            return self.task.period < other.task.period
        else:
            return self.task.arrival < other.task.arrival
