import abc
import csv
import json
import os
import random
from typing import List

from execution_profile import ExecutionProfile
from task import Task


class TaskGenerator(abc.ABC):
    def __init__(self) -> None:
        pass

    @staticmethod
    def uunifast_discard(n, u, nsets):
        sets = []
        while len(sets) < nsets:
            utilizations = []
            sumU = u
            for i in range(1, n):
                nextSumU = sumU * random.random() ** (1.0 / (n - i))
                utilizations.append(sumU - nextSumU)
                sumU = nextSumU
            utilizations.append(sumU)

            if all(ut <= 1 for ut in utilizations):
                sets.append(utilizations)

        return sets

    @staticmethod
    def generate_utilization_files(nsets):
        profile_directory_path = 'gpu_t400/profiles'
        utilizations_directory_path = 'gpu_t400/utilizations'
        task_names = [file.replace('.csv', '') for file in os.listdir(profile_directory_path) if file.endswith('.csv')]
        util_sets = TaskGenerator.uunifast_discard(len(task_names), 6, nsets)
        for i in range(nsets):
            task_set = {task_names[j]: util_sets[i][j] for j in range(len(task_names))}
            with open(os.path.join(utilizations_directory_path, f'taskset_{i + 1}.json'), 'w') as f:
                json.dump(task_set, f)

    @staticmethod
    def add_profiles_to_task(task: Task) -> None:
        profile_directory_path = 'gpu_t400/profiles'
        with open(os.path.join(profile_directory_path, f'{task.name}.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                sm_count = int(row[0])
                average = float(row[1])
                min_val = float(row[2])
                max_val = float(row[3])
                power = float(row[4])
                energy = float(row[5])
                energy_in_window = float(row[6])
                execution_profile = ExecutionProfile(average, min_val, max_val, power, energy, energy_in_window)
                task.add_execution_profile(sm_count, execution_profile)

    @staticmethod
    @abc.abstractmethod
    def generate_tasks(task_set_file_path: str = 'gpu_t400/utilizations/taskset_1.json') -> List[Task]:
        pass


class MinExecTaskGenerator(TaskGenerator):

    @staticmethod
    def generate_tasks(task_set_file_path: str = 'gpu_t400/utilizations/taskset_1.json') -> List[Task]:
        all_tasks = []
        with open(task_set_file_path, 'r') as f:
            task_utils = json.load(f)
        for task_name, utilization in task_utils.items():
            task = Task(name=task_name, arrival_time=0)
            MinExecTaskGenerator.add_profiles_to_task(task)
            task.execution_time = task.execution_profiles[1].min
            task.util = utilization
            task.period = task.execution_time / utilization
            all_tasks.append(task)

        random.shuffle(all_tasks)
        for i in range(len(task_utils)):
            all_tasks[i].index = i

        return all_tasks


class AvgExecTaskGenerator(TaskGenerator):

    @staticmethod
    def generate_tasks(task_set_file_path: str = 'gpu_t400/utilizations/taskset_1.json') -> List[Task]:
        all_tasks = []
        with open(task_set_file_path, 'r') as f:
            task_utils = json.load(f)
        for task_name, utilization in task_utils.items():
            task = Task(name=task_name, arrival_time=0)
            MinExecTaskGenerator.add_profiles_to_task(task)
            task.execution_time = task.execution_profiles[1].average
            task.util = utilization
            task.period = task.execution_time / utilization
            all_tasks.append(task)

        random.shuffle(all_tasks)
        for i in range(len(task_utils)):
            all_tasks[i].index = i

        return all_tasks


class MaxExecTaskGenerator(TaskGenerator):

    @staticmethod
    def generate_tasks(task_set_file_path: str = 'gpu_t400/utilizations/taskset_1.json') -> List[Task]:
        all_tasks = []
        with open(task_set_file_path, 'r') as f:
            task_utils = json.load(f)
        for task_name, utilization in task_utils.items():
            task = Task(name=task_name, arrival_time=0)
            MinExecTaskGenerator.add_profiles_to_task(task)
            task.execution_time = task.execution_profiles[1].max
            task.util = utilization
            task.period = task.execution_time / utilization
            all_tasks.append(task)

        random.shuffle(all_tasks)
        for i in range(len(task_utils)):
            all_tasks[i].index = i

        return all_tasks
