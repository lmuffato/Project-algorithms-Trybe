def study_schedule(permanence_period, target_time):
    student_counter = 0
    for time_period in permanence_period:
        try:
            if time_period[0] <= target_time <= time_period[1]:
                student_counter += 1
        except TypeError:
            return None
    return student_counter
