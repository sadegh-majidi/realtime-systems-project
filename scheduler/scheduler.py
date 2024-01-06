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
        i = 0
        scheduled_logs = {}
        for task in self.controller.tasks:
            scheduled_logs[task.name] = []
        while current_time < self.hyper_period:
            first_task, second_task = self.controller.get_task_to_execute(remaining_cores)
            if current_time < first_task.arrival and current_time < second_task.arrival:
                current_time += min(first_task.arrival, second_task.arrival)

            if not first_task.executed:
                if first_task.arrival <= current_time:
                    print(f"Executing task #{first_task.name} on #{first_task.cores} cores")
                    scheduled_logs[first_task.name].append(current_time)
                    remaining_cores -= first_task.cores
                    first_task.executed = True

            if not second_task.executed:
                if second_task.arrival <= current_time:
                    print(f"Executing task #{second_task.name} on #{second_task.cores} cores")
                    scheduled_logs[second_task.name].append(current_time)
                    remaining_cores -= second_task.cores
                    second_task.executed = True

            execution_time = 0.1
            # execution_time = min(first_task.execution_time, second_task.execution_time)
            current_time += execution_time

            first_task.execution_time -= execution_time
            second_task.execution_time -= execution_time

            if first_task.execution_time <= 0:
                if first_task.arrival + first_task.period < current_time:
                    print(f"Task #{first_task.name} missed its deadline!!!!")
                else:
                    print(f"Task #{first_task.name} executed")
                scheduled_logs[first_task.name].append(current_time)
                remaining_cores += first_task.cores
                first_task.arrival += first_task.period
                first_task.cores = None
                first_task.execution_time = None
                first_task.executed = False

            if second_task.execution_time <= 0:
                if second_task.arrival + second_task.period < current_time:
                    print(f"Task #{second_task.name} missed its deadline!!!!")
                else:
                    print(f"Task #{second_task.name} executed")
                scheduled_logs[second_task.name].append(current_time)
                remaining_cores += second_task.cores
                second_task.arrival += second_task.period
                second_task.cores = None
                second_task.execution_time = None
                second_task.executed = False

            self.controller.add_task_to_queue(first_task)
            self.controller.add_task_to_queue(second_task)
            i += 1
        return scheduled_logs
