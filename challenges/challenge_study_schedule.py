def is_student_time_valid(student_hours):
    if not isinstance(student_hours[0], int):
        return False
    if not isinstance(student_hours[1], int):
        return False
    return True


def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for student in permanence_period:
        if not is_student_time_valid(student):
            return None
        if student[0] <= target_time <= student[1]:
            counter += 1

    return counter
