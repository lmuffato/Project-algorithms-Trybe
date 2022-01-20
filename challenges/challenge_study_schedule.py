
def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for each_schedule in permanence_period:
        if not each_schedule[0] or not each_schedule[1]:
            return None
        elif each_schedule[0] <= target_time <= each_schedule[1]:
            count += 1
    return count
