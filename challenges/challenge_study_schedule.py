def study_schedule(permanence_period, target_time):
    n_estudantes = 0
    for student in permanence_period:
        if student[0] <= target_time and student[1] >= target_time:
            n_estudantes += 1
    return n_estudantes
