import os

from parser import CSVParser

if __name__ == '__main__':
    directory_path = 'gpu_t400'
    all_tasks = []

    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        task = CSVParser.parse(file_path)
        all_tasks.append(task)
