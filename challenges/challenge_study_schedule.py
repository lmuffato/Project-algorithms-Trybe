def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for period in permanence_period:
        if not period[0] or not period[1]:
            return None
        if target_time >= period[0] and target_time <= period[1]:
            counter += 1

    return counter
