def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for time in permanence_period:
        if time[0] is None or time[1] is None:
            return None
        if time[0] <= target_time and time[1] >= target_time:
            count += 1
    return count
