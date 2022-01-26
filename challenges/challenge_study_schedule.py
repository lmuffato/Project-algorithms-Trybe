def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for i in permanence_period:
            if target_time >= i[0] and target_time <= i[1]:
                count += 1
    except TypeError:
        return None
    return count
