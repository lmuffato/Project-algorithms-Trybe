def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for start_time, exit_time in permanence_period:
            if start_time <= target_time <= exit_time:
                students += 1
        return students
    except TypeError:
        return None
