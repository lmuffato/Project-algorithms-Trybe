def study_schedule(permanence_period, target_time):
    result = 0
    if not target_time:
        return None
    for period in permanence_period:
        if None in period:
            return None
        elif period[0] <= target_time <= period[1]:
            result += 1
    return result
