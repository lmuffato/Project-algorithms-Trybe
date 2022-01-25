def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if target_time is None:
        return None

    for period in permanence_period:
        if period[0] is None or period[1] is None:
            return None
        if target_time >= period[0] and target_time <= period[1]:
            counter += 1

    return counter
