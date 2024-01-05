from execution_profile import ExecutionProfile


class Task:
    def __init__(self, name: str, arrival_time) -> None:
        self.name = name
        self.arrival = arrival_time
        self.execution_time = None
        self.execution_profiles = {}

    def __lt__(self, other):
        return self.arrival < other.arrival

    def add_execution_profile(self, sm_count: int, execution_profile: ExecutionProfile) -> None:
        self.execution_profiles[sm_count] = execution_profile
