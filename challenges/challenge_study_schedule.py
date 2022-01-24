def study_schedule(permanence_period, target_time):
    n_estudantes = 0
    if target_time == '':
        return None
    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None
        if student[0] <= target_time and student[1] >= target_time:
            n_estudantes += 1
    return n_estudantes
