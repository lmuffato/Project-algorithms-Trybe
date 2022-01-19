def study_schedule(permanence_period, target_time):
    if (permanence_period or target_time) == '':
        return None
    else:
        best_hour = 0
        for begin, end in permanence_period:
            if begin == None or end == None:
                return None
            if (begin <= target_time) and (end >= target_time):
                best_hour += 1
    return best_hour
