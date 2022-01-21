def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    count_students = 0
    if not target_time or type(target_time) != int:
        return None
    else:
        for student in permanence_period:
            if type(student[0]) == int and type(student[1]) == int:
                if student[0] <= target_time and student[1] >= target_time:
                    count_students = count_students + 1
            else:
                return None
        return count_students
