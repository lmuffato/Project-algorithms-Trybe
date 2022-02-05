def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    online_students = 0
    for in_time, out_time in permanence_period:
        if not in_time or not out_time:
            return None
        if in_time <= target_time <= out_time:
            online_students += 1
    return online_students
