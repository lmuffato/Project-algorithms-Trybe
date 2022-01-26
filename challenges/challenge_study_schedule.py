def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    index = 0
    for indice in permanence_period:
        if indice[0] is None or indice[1] is None:
            return None
        elif indice[0] <= target_time <= indice[1]:
            index += 1

    return index
