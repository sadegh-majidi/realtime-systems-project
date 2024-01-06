import heapq


class Scheduler:

    def __init__(self, hyper_period, controller):
        self.hyper_period = hyper_period
        self.controller = controller

    def run_FCFS_schedule(self):
        current_time = 0

        while current_time <= self.hyper_period:
            active_task = self.controller.get_task_to_execute()
            print(f"Executing task #{active_task.name}")
            current_time += active_task.execution_time
            print(f"Task #{active_task.name} executed")
            active_task.task.arrival += active_task.period
            self.controller.add_task_to_queue(active_task)

    def run_sBEET_schedule(self):
        current_time = 0
        remaining_cores = 6
        while current_time < self.hyper_period:
            first_task, second_task = self.controller.get_task_to_execute(remaining_cores)
            remaining_cores = 6
            remaining_cores -= first_task.cores + second_task.cores

            print(f"Executing task #{first_task.name} on #{first_task.cores} cores")
            print(f"Executing task #{second_task.name} on #{second_task.cores} cores")

            execution_time = min(first_task.execution_time, second_task.execution_time)
            current_time += execution_time

            first_task.execution_time -= execution_time
            second_task.execution_time -= execution_time

            if first_task.execution_time == 0:
                print(f"Task #{first_task.name} executed")
                remaining_cores += first_task.cores
                first_task.arrival += first_task.period
                first_task.cores = None
                first_task.execution_time = None

            if second_task.execution_time == 0:
                print(f"Task #{second_task.name} executed")
                remaining_cores += second_task.cores
                second_task.arrival += second_task.period
                second_task.cores = None
                second_task.execution_time = None

            self.controller.add_task_to_queue(first_task)
            self.controller.add_task_to_queue(second_task)
