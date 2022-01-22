def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None
    present_students = 0
    for time_student_tuple in permanence_period:
        if None in time_student_tuple:
            return None
        if time_student_tuple[0] <= target_time <= time_student_tuple[1]:
            present_students += 1
    return present_students
