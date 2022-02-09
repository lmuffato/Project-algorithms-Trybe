def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    platform_access = 0

    for entry, exit in permanence_period:
        if not target_time:
            return None
        if not entry or not exit:
            return None
        if entry <= target_time <= exit:
            platform_access += 1
    return platform_access
