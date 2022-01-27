def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students = 0
    if target_time is None:
        return None
    else:
        for n in permanence_period:
            entry = n[0]
            exit = n[1]
            if entry <= target_time and exit >= target_time:
                students += 1
        return students

