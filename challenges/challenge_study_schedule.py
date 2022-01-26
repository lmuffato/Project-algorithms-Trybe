def study_schedule(permanence_period, target_time):
    count = 0
    for student in permanence_period:
        if not target_time or not student[0] or not student[1]:
            return None

        if target_time >= student[0] and target_time <= student[1]:
            count += 1
    return count
