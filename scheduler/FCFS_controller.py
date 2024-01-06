import heapq


class FSFCController:
    def __init__(self, tasks):
        self.tasks = tasks
        self.tasks_queue = []

    def init_task_queue(self):
        for task in self.tasks:
            heapq.heappush(self.tasks_queue, task)
        return self

    def get_task_to_execute(self):
        return heapq.heappop(self.tasks_queue)

    def add_task_to_queue(self, task):
        heapq.heappush(self.tasks_queue, task)
