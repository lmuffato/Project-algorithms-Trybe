def study_schedule(permanence_period, target_time):
    counter = 0
    if(not target_time):
        return None
    for period in permanence_period:
        low, high = period
        if(not low or not high):
            return None
        if(low <= target_time <= high):
            counter += 1

    return counter
