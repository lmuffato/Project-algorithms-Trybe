def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    else:
        counter = 0
        for (start, end) in permanence_period:
            if start <= target_time and end >= target_time:
                counter += 1
    return counter
