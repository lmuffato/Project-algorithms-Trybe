def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if not target_time:
        return None
    sum_studentes = 0
    for student in permanence_period:
        # usei o not pois o type o teste não passava!!!
        if not student[0] or not student[1]:
            return None
        if student[0] <= target_time and student[1] >= target_time:
            sum_studentes += 1

    return sum_studentes
