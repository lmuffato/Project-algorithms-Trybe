def study_schedule(permanence_period, target_time):
    if (permanence_period[0][0] is None or permanence_period[0][1] is None):
        return None
    if (target_time is None):
        return None

    students = 0
    for study_time in permanence_period:
        if (study_time[0] <= target_time <= study_time[1]):
            students += 1
    return students
