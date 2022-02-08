def study_schedule(permanence_period, target_time):
    student = 0
    try:
        for entry_time, exit_time in permanence_period:
            if entry_time <= target_time <= exit_time:
                student += 1
        return student
    except TypeError:
        return None