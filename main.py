import math
from task_gen import TaskGenerator
from scheduler.wrapped_classes import FCFSTaskWrapper, sBEETTaskWrapper
from scheduler.scheduler import Scheduler
from scheduler.FCFS_controller import FSFCController
from scheduler.sBEET_controller import sBEETController
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_plot_for_FCFS_tasks(tasks):
    for task in tasks:
        values = tasks[task]

        fig, ax = plt.subplots()
        y_value = 0.5
        # x_ticks = [segment[0] for segment in executed_slots]
        for segment in values:
            width = segment[1] - segment[0]
            rect = patches.Rectangle((segment[0], y_value - 0.5), width, 1, linewidth=0, edgecolor='lightblue',
                                     facecolor='lightblue')
            ax.add_patch(rect)

        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        # ax.set_xticks(x_ticks)
        plt.xlim(0, 10000)
        plt.ylim(0, 2)

        plt.xlabel('time')
        plt.ylabel('y')
        plt.title(f'{task}')

        plt.show()


def create_plot_for_sBEET_tasks(tasks):
    for task in tasks:
        values = tasks[task]
        executed_slots = []
        for i in range(0, len(values) - 1, 2):
            executed_slots.append((values[i], values[i + 1]))
        fig, ax = plt.subplots()

        y_value = 0.5
        # x_ticks = [segment[0] for segment in executed_slots]
        for segment in executed_slots:
            width = segment[1] - segment[0]
            rect = patches.Rectangle((segment[0], y_value - 0.5), width, 1, linewidth=0, edgecolor='lightblue',
                                     facecolor='lightblue')
            ax.add_patch(rect)

        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        # ax.set_xticks(x_ticks)
        plt.xlim(0, 10000)
        plt.ylim(0, 2)

        plt.xlabel('time')
        plt.ylabel('y')
        plt.title(f'{task}')

        plt.show()


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
    scheduler = Scheduler(hyper_period=10000, controller=fsfc_controller)
    scheduled_logs, power_logs = scheduler.run_FCFS_schedule()
    # create_plot_for_FCFS_tasks(scheduled_logs)
    print(power_logs)

    # sbeet_controller = sBEETController(sbeet_tasks).init_task_queue()
    # scheduler = Scheduler(hyper_period=10000, controller=sbeet_controller)
    # scheduled_tasks = scheduler.run_sBEET_schedule()
    # create_plot_for_sBEET_tasks(scheduled_tasks)
