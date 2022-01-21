def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    hit_target = 0
    for tupla in permanence_period:
        if tupla[0] is None or tupla[1] is None:
            return None
        elif tupla[0] <= target_time <= tupla[1]:
            hit_target += 1

    return hit_target
