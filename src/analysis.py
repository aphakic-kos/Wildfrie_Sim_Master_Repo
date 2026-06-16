import os
import numpy as np

try:
    from core.board import BARRIER, BURNING, BURNT
    from core.engine import Engine
except ImportError:
    from board import BARRIER, BURNING, BURNT
    from engine import Engine


class Analysis:
    def __init__(self):
        pass

    @staticmethod
    def percentage_of_burnt_area(map_obj, exclude_barriers=True):
        curr_map = map_obj.curr_map
        burnt_cells = np.count_nonzero(curr_map == BURNT)

        if exclude_barriers:
            total_cells = np.count_nonzero(curr_map != BARRIER)
        else:
            total_cells = curr_map.size

        if total_cells == 0:
            return 0.0

        return burnt_cells / total_cells * 100.0

    @staticmethod
    def currently_burning_cells(map_obj):
        return np.argwhere(map_obj.curr_map == BURNING)

    @staticmethod
    def number_of_burning_cells(map_obj):
        return np.count_nonzero(map_obj.curr_map == BURNING)

    @staticmethod
    def wildfire_duration(map_obj):
        """
        Run one full simulation and return its real duration.
        This assumes Engine.simulation(map_obj) returns total_time.
        """
        return Engine.simulation(map_obj)

    @staticmethod
    def statistical_experiment(
        map_obj,
        N,
        output_dir="data",
        duration_filename="durations.npy",
        burnt_percentage_filename="burnt_percentages.npy",
        exclude_barriers=True,
    ):
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        os.makedirs(output_dir, exist_ok=True)

        durations = np.zeros(N, dtype=np.int32)
        burnt_percentages = np.zeros(N, dtype=np.float32)

        initial_ignited_map = map_obj.curr_map.copy()

        for i in range(N):
            map_obj.curr_map = initial_ignited_map.copy()

            durations[i] = Analysis.wildfire_duration(map_obj)

            burnt_percentages[i] = Analysis.percentage_of_burnt_area(
                map_obj,
                exclude_barriers=exclude_barriers,
            )

        np.save(os.path.join(output_dir, duration_filename), durations)
        np.save(os.path.join(output_dir, burnt_percentage_filename), burnt_percentages)

        return durations, burnt_percentages
