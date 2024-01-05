class ExecutionProfile:
    def __init__(self, average: float, min_val: float, max_val: float, power: float, energy: float,
                 energy_in_window: float) -> None:
        self.average = average
        self.min = min_val
        self.max = max_val
        self.power = power
        self.energy = energy
        self.energy_in_window = energy_in_window
