def study_schedule(permanence_period, target_time):
    count = 0
    for (first, second) in permanence_period:
        try:
            if first <= int(target_time) <= second:
                count += 1
        except TypeError:
            return None
    return count
