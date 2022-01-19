def study_schedule(permanence_period, target_time):
    count = 0
    for (first, second) in permanence_period:
        try:
            if int(target_time) in range(first, second+1):
                count += 1
        except TypeError:
            return None
    return count
