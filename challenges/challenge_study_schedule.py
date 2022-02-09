def study_schedule(permanence_period, target_time):
    count = 0

    if not target_time:
        return None

    for entry, exit in permanence_period:
        if not entry or not exit:
            return None
        if entry <= target_time <= exit:
            count += 1

    return count
