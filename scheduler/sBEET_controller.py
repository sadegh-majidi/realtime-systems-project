import heapq
import math

min_route = []
min_exec_time = math.inf
min_power = math.inf


class sBEETController:
    def __init__(self, tasks):
        self.tasks = tasks
        self.tasks_queue = []

    def init_task_queue(self):
        for task in self.tasks:
            heapq.heappush(self.tasks_queue, task)
        return self

    # def get_two_task_to_execute(self):
    #     first_task = heapq.heappop(self.tasks_queue)
    #     second_task = heapq.heappop(self.tasks_queue)
    #
    #     # first_task, second_task, total_exec_time, total_power
    #     best_choice = {"first_task": None, "second_task": None, "best_time": math.inf, "best_power": math.inf}
    #     for core in range(6, 0, -1):
    #         first_task_exec_time = first_task.execution_profile[core].exec_time
    #         second_task_exec_time = first_task.execution_profile[6 - core].exec_time
    #         total_exec_time = first_task_exec_time + second_task_exec_time
    #
    #         first_task_power = first_task.execution_profile[core].power
    #         second_task_power = first_task.execution_profile[6 - core].power
    #         total_power = first_task_power + second_task_power
    #
    #         if total_exec_time < best_choice["best_time"]:
    #             best_choice = {"first_task": first_task, "second_task": second_task, "best_time": total_exec_time,
    #                            "best_power": total_power}
    #
    #         elif best_choice["best_time"] == total_exec_time:
    #             if total_power < best_choice["best_power"]:
    #                 best_choice = {"first_task": first_task, "second_task": second_task, "best_time": total_exec_time,
    #                                "best_power": total_power}
    #     return best_choice

    # def get_one_task_to_execute(self, total_exec_time, total_power):
    #     first_task = heapq.heappop(self.tasks_queue)
    #     total_exec_time += first_task.execution_profile[6].exec_time
    #     total_power += first_task.execution_profile[6].exec_time
    #
    # def get_best_route_to_execute(self, i, total_exec_time, total_power):
    #     global min_exec_time, min_power, min_route
    #
    #     if len(self.tasks_queue) == 0:
    #         return
    #
    #     if i == 0:
    #         self.get_two_task_to_execute()
    #     else:
    #         self.get_one_task_to_execute(total_exec_time, total_power)
    #
    #     self.get_best_route_to_execute(0, total_exec_time, total_power)
    #     self.get_best_route_to_execute(i, total_exec_time, total_power)

    def get_task_to_execute(self, remaining_cores):
        if remaining_cores != 6:
            first_task = heapq.heappop(self.tasks_queue)
            second_task = heapq.heappop(self.tasks_queue)
            second_task.cores = 6 - remaining_cores
            second_task.execution_time = second_task.execution_profiles[6 - remaining_cores].exec_time
            return first_task, second_task
        else:
            first_task = heapq.heappop(self.tasks_queue)
            second_task = heapq.heappop(self.tasks_queue)
            # first_task, second_task, total_exec_time, total_power
            best_choice = {"first_task": None, "second_task": None, "best_time": math.inf, "best_power": math.inf}
            final_tasks = None
            for core in range(5, 1, -1):
                first_task_exec_time = first_task.execution_profiles[core].exec_time
                second_task_exec_time = second_task.execution_profiles[6 - core].exec_time
                total_exec_time = first_task_exec_time + second_task_exec_time

                first_task_power = first_task.execution_profiles[core].power
                second_task_power = second_task.execution_profiles[6 - core].power
                total_power = first_task_power + second_task_power

                if total_exec_time < best_choice["best_time"]:
                    best_choice = {"first_task": first_task, "second_task": second_task, "best_time": total_exec_time,
                                   "best_power": total_power}
                    final_tasks = (
                        (first_task, core, first_task_exec_time), (second_task, 6 - core, second_task_exec_time))

                elif best_choice["best_time"] == total_exec_time:
                    if total_power < best_choice["best_power"]:
                        best_choice = {"first_task": first_task, "second_task": second_task,
                                       "best_time": total_exec_time,
                                       "best_power": total_power}
                        final_tasks = (
                            (first_task, core, first_task_exec_time), (second_task, 6 - core, second_task_exec_time))

            first_task = final_tasks[0][0]
            second_task = final_tasks[1][0]

            first_task.execution_time = final_tasks[0][2]
            first_task.cores = final_tasks[0][1]

            second_task.execution_time = final_tasks[1][2]
            second_task.cores = final_tasks[1][1]

            return first_task, second_task

    def add_task_to_queue(self, task):
        heapq.heappush(self.tasks_queue, task)
