def study_schedule(permanence_period, target_time):

    if target_time is None:
        return target_time

    count = 0

    for a, b in permanence_period:
        if a is None or b is None:
            return None

        if a <= target_time and b >= target_time:
            count += 1
    return count
