def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for (start, end) in permanence_period:
            if start <= target_time and end >= target_time:
                counter += 1
        return counter
    except TypeError:
        return None
