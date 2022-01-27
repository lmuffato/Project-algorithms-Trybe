def occurrences(permanence_period, target_time):
    occurrence = 0
    for period in permanence_period:
        if period[0] <= target_time <= period[1]:
            occurrence += 1

    return occurrence


def study_schedule(permanence_period, target_time):
    try:
        if target_time >= 0:
            return occurrences(permanence_period, target_time)

        return None
    except TypeError:
        return None
