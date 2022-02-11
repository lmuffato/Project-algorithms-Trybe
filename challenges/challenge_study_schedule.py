def study_schedule(permanence_period, target_time):
    students_on = 0

    if not target_time:
        return None

    for in_time, out_time in permanence_period:
        if not in_time or not out_time:
            return None
        if in_time <= target_time <= out_time:
            students_on += 1

    return students_on
