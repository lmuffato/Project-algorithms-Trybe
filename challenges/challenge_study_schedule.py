def study_schedule(permanence_period, target_time):
    num = 0
    for hrs in permanence_period:
        if None in hrs or target_time is None:
            return None

        if hrs[0] <= target_time <=hrs[1]:
            num += 1
    return num