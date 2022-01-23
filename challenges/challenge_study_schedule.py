def study_schedule(permanence_period, target_time):
    counter = 0
    for row in permanence_period:
        try:
            if row[0] <= target_time <= row[1]:
                counter += 1
        except TypeError:
            return None
    return counter
