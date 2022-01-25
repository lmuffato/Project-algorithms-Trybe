def study_schedule(permanence_period, target_time):
    if (permanence_period[0][0] is None or permanence_period[0][1] is None):
        return None
    if (target_time is None):
        return None
    STUDIES = 0
    for DATA in permanence_period:
        if (DATA[0] <= target_time <= DATA[1]):
            STUDIES += 1
    return STUDIES
