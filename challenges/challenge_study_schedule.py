def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    student_count = 0
    for time_period in permanence_period:
        if time_period[0] is None or time_period[1] is None:
            return None

        if target_time >= time_period[0] and target_time <= time_period[1]:
            student_count += 1

    return student_count
