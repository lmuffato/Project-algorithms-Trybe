def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    max_value = 0
    for entrance, leave in permanence_period:
        if entrance <= target_time:
            if target_time <= leave:
                max_value += 1
        else:
            return None
    return max_value
