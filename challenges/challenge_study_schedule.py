def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    else:
        counter = 0
        for one_period in permanence_period:
            if not all(one_period):
                return None
            if one_period[0] <= target_time <= one_period[1]:
                counter += 1
    return counter