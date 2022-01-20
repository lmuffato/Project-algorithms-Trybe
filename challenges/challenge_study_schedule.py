def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    sum = 0
    for period in permanence_period:
        if period[0] is None or period[1] is None:
            return None
        if period[0] <= target_time <= period[1]:
            sum += 1

    return sum
