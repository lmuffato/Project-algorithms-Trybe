def study_schedule(permanence_period, target_time):
    try:
        max = 0

        for period in permanence_period:
            if period[0] is target_time or period[1] is target_time:
                max += 1

        return max

    except TypeError:
        return None
