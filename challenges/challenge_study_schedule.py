def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None

    counter = 0
    for first, second in permanence_period:
        if first and second is None:
            return None
        if first <= target_time and target_time <= second:
            counter += 1
    return counter
