from task_gen import TaskGenerator

if __name__ == '__main__':
    tasks = TaskGenerator(gen_type=TaskGenerator.MAX).generate_tasks()
