def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for enter, exit in permanence_period:
            if enter <= target_time <= exit:
                counter += 1
        return counter
    except TypeError:
        return None
