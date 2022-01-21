def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for student_p in permanence_period:
        if student_p[0] is None or student_p[1] is None:
            return None
        if target_time >= student_p[0] and target_time <= student_p[1]:
            count += 1
    return count


"""
    cada tupla (horario_entrada, horario_saida)
"""