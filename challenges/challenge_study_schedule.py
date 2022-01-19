def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    _count = 0

    for period in permanence_period:
        if period[0] is None or period[1] is None:
            return None
        if period[1] >= target_time and period[0] <= target_time:
            _count += 1

    return _count
