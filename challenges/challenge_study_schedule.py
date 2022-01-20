def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time == None:
        return None
    counter = 0
    for period in permanence_period:
        if type(period[0]) == int and type(period[1]) == int:
            if period[0] <= target_time <= period[1]:
                counter += 1
        else:
            return None
            break
    return counter
