permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 5


def study_schedule(permanence_period, target_time):
    try:
        max = 0

        for period in permanence_period:
            if period[0] is target_time or period[1] is target_time:
                max += 1

        return max

    except TypeError:
        return None
