def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    else:
        best_schedule = 0
        for start, end in permanence_period:
            if start is None or end is None:
                return None
            if (start <= target_time) and (end >= target_time):
                best_schedule += 1
    return best_schedule
