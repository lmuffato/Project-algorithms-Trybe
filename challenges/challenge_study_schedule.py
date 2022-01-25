def study_schedule(permanence_period, target_time):
    index = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                index += 1
        return index
    except TypeError:
        return None
