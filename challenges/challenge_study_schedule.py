def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for student_in, student_out in permanence_period:
            if student_in <= target_time <= student_out:
                students += 1
        return students
    except TypeError:
        raise None
