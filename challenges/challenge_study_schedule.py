def study_schedule(permanence_period, target_time):
    sum = 0
    for (beginning_time, end_time) in permanence_period:
        if beginning_time is None or end_time is None or target_time is None:
            return None
        else:
            if beginning_time <= target_time <= end_time:
                sum += 1
    return sum
