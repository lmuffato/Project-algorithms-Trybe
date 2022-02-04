def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    n = 0
    for i in permanence_period:
        if i[0] is None or i[1] is None:
            return None
        elif i[0] <= target_time <= i[1]:
            n += 1

    return n
