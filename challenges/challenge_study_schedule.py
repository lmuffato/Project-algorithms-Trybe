def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for check_in, check_out in permanence_period:
        if not isinstance(check_in, int) or not isinstance(check_out, int):
            return None
        if check_in <= target_time <= check_out:
            counter += 1

    return counter
