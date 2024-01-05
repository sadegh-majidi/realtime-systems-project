import csv

from execution_profile import ExecutionProfile
from task import Task


class CSVParser:

    @staticmethod
    def parse(file_path: str) -> Task:
        task_name = file_path.split('/')[-1].replace('.csv', '')
        task = Task(task_name)
        with open(file_path, 'r') as csv_file:
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

        return task
