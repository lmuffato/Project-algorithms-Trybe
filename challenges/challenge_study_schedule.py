def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for student in permanence_period:
        if not student[0] or not student[1]:
            return None
        if student[0] <= target_time <= student[1]:
            count += 1

    return count
