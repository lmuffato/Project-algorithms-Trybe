def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    total = 0
    if target_time is None:
        return None
    for tupla in permanence_period:
        if tupla[0] is None or tupla[1] is None:
            return None
        elif tupla[0] <= target_time <= tupla[1]:
            total += 1
    return total
