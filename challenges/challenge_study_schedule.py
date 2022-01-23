def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    students_in = 0
    for in_time, out_time in permanence_period:
        if in_time is None or out_time is None:
            return None
        if in_time <= target_time <= out_time:
            students_in += 1
    return students_in
