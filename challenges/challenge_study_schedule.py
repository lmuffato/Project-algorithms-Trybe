def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    try:
        max_value = 0
        for entrance, leave in permanence_period:
            if entrance <= target_time <= leave:
                max_value += 1
    except TypeError:
        return None

    return max_value
