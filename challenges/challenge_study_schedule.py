from audioop import reverse


def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for item in permanence_period:
            if target_time >= item[0] and target_time <= item[1]:
                count += 1
        return count
    except TypeError:
        return None
