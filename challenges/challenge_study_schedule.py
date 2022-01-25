def study_schedule(permanence_period, target_time):
    if (permanence_period[0][0] is None or permanence_period[0][1] is None):
        return None
    if (target_time is None):
        return None
    people = 0
    for schedule_period in permanence_period:
        if (schedule_period[0] <= target_time <= schedule_period[1]):
            people += 1
    return people
