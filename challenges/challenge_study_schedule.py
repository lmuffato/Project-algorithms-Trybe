def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students = 0
    if target_time is None:
        return None
    else:
        for time in permanence_period:
            if int(all(time)):
                entry = time[0]
                exit = time[1]
                if entry <= target_time and exit >= target_time:
                    students += 1
            else:
                return None
        return students
