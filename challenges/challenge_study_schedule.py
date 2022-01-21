def study_schedule(permanence_period, target_time):
    count = 0

    for (entry, exit) in permanence_period:
        try:
            if entry <= int(target_time) <= exit:
                count += 1
        except TypeError:
            return None
    return count
