def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None
    count = 0
    for studant_period in permanence_period:
        try:
            if studant_period[0] <= target_time <= studant_period[1]:
                count += 1
        except TypeError:
            return None
    return count
