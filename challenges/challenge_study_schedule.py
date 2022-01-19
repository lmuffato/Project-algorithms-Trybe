def study_schedule(permanence_period, target_time):
    ocorrence_target = 0

    if int != type(target_time):
        return None

    for key, element in permanence_period:
        if key is None or element is None:
            return None
        elif key <= target_time <= element:
            ocorrence_target += 1
    return ocorrence_target
