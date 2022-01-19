def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    contador = 0
    if target_time is None:
        return None
    for period_1, period_2 in permanence_period:
        if type(period_1) != int or type(period_2) != int:
            return None
        elif target_time >= period_1 and target_time <= period_2:
            contador += 1
    return contador
