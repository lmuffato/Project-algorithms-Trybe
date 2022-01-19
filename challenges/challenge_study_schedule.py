def study_schedule(permanence_period, target_time):

    if target_time == None:
        return target_time

    count = 0

    for a, b in permanence_period:
        if a == None or b == None:
            return None

        if a <= target_time and b >= target_time:
            count += 1
    return count
