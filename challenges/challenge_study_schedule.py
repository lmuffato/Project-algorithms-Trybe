def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if (target_time is None):
        return None
    else:
        count = 0
        for login, logout in permanence_period:
            if login is None or logout is None:
                return None
            if (login <= target_time) and (logout >= target_time):
                count += 1
    return count
