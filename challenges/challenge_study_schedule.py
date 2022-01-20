def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for time in permanence_period:
            if target_time >= time[0] and target_time <= time[1]:
                counter += 1
    except TypeError:
        return None
    return counter
