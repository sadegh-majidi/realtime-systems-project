import heapq


class Scheduler:

    def __init__(self, tasks, hyper_period, controller):
        self.tasks = tasks
        self.hyper_period = hyper_period
        self.controller = controller

    def setup_controller(self):
        self.controller.init_task_queue()

    def run_FCFS_schedule(self):
        current_time = 0

        while current_time <= self.hyper_period:
            active_task = self.controller.get_task_to_execute()
            print(f"Executing task #{active_task.name}")
            current_time += active_task.executation_time
            print(f"Task #{active_task.name} executed")

    def run_sBEET_schedule(self):
        pass
