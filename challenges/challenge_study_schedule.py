def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None
    counter = 0

    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                counter += 1
        except TypeError:
            return None
    return counter
