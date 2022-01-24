def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if target_time is None:
        return None
    for period in permanence_period:
        # Se o valor inicial ou final for igual a 0 ou invalido
        if not period[0] or not period[1]:
            return None
        # Se o valor do target_time for maior/igual que o inicial
        # E o target_time for menor/igual ao final
        elif target_time >= period[0] and target_time <= period[1]:
            counter += 1
    return counter


# print(study_schedule([(2, 1), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
