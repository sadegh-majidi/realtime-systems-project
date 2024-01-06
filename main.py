import math
from task_gen import TaskGenerator
from scheduler.wrapped_classes import FCFSTaskWrapper, sBEETTaskWrapper
from scheduler.scheduler import Scheduler
from scheduler.FCFS_controller import FSFCController


def wrap_tasks(schedule_wrapper, tasks):
    return [schedule_wrapper(task) for task in tasks]


def wrap_tasks_for_FCFS_schedule(tasks):
    return wrap_tasks(FCFSTaskWrapper, tasks)


def wrap_tasks_for_sBEET_schedule(tasks):
    return wrap_tasks(sBEETTaskWrapper, tasks)


def calculate_hyper_period(tasks_set):
    def lcm(a, b):
        return int(abs(a * b)) // math.gcd(int(a), int(b))

    current_hyper_period = tasks_set[0].period
    for task in tasks_set[1:]:
        current_hyper_period = lcm(current_hyper_period, task.period)

    return current_hyper_period


if __name__ == '__main__':
    tasks = TaskGenerator(gen_type=TaskGenerator.MAX).generate_tasks()
    fcfs_tasks = wrap_tasks_for_FCFS_schedule(tasks)
    sbeet_tasks = wrap_tasks_for_sBEET_schedule(tasks)

    hyper_period = calculate_hyper_period(fcfs_tasks)
    fsfc_controller = FSFCController(fcfs_tasks).init_task_queue()
    scheduler = Scheduler(hyper_period=hyper_period, controller=fsfc_controller)
    scheduler.run_FCFS_schedule()
