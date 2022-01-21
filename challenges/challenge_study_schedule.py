def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for student_period in permanence_period:
        if student_period[0] is None or student_period[1] is None:
            return None
        if target_time >= student_period[0] and target_time <= student_period[1]:
            count += 1
    return count


"""
    cada tupla (horario_entrada, horario_saida)
"""