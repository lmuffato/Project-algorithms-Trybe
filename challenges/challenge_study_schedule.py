def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    else:
        iterator = 0
        for run_time in permanence_period:
            if run_time[0] is None or run_time[1] is None:
                return None
            if run_time[0] <= target_time and run_time[1] >= target_time:
                iterator += 1
    return iterator
