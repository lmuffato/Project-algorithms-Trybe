def study_schedule(permanence_period, target_time):
    number_of_students = 0

    if target_time is None:
        return None

    for student_time in permanence_period:

        index = 0

        if student_time[index] is None or student_time[index + 1] is None:
            return None

        if student_time[index] <= target_time <= student_time[index + 1]:
            number_of_students += 1

    return number_of_students
