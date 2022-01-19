def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for student in permanence_period:
            if student[0] <= target_time <= student[1]:
                counter +=1
        return counter
    except TypeError:
        return None

