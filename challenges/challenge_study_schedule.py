def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    matchHorario = 0
    if target_time is None:
        return None
    for [horario1, horario2] in permanence_period:
        if (not horario1 or not horario2):
            return None
        if horario1 <= target_time <= horario2:
            matchHorario += 1
    return matchHorario
    