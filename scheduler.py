import heapq


class Scheduler:

    def __init__(self, tasks, hyper_period):
        self.tasks = tasks
        self.hyper_period = hyper_period

    def run_FCFS_schedule(self):
        tasks_queue = []
        for task in self.tasks:
            heapq.heappush(tasks_queue, task)

        current_time = 0

        while current_time <= self.hyper_period:
            active_task = heapq.heappop(tasks_queue)
            print(f"Executing task #{active_task.name}")
            current_time += active_task.executation_time
            print(f"Task #{active_task.name} executed")
