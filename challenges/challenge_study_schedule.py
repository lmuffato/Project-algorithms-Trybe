def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if type(target_time) != int:
        return None

    hit_target = 0
    for tupla in range(len(permanence_period)):
        if target_time >= tupla[0] or target_time >= tupla[1]:
            hit_target += 1

    return hit_target
