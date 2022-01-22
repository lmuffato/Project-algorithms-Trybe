def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None
    counter = 0
    for permanence_tuple in permanence_period:
        if None in permanence_tuple:
            return None
        if permanence_tuple[0] <= target_time <= permanence_tuple[1]:
            counter += 1
    return counter
