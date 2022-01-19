from typing import Counter


def study_schedule(permanence_period, target_time):
    if target_time == 0:
        return None
    else:
        counter = 0
        for element in permanence_period:
            a = element[0]
            b = element[1]
            if a < 0 or b < 0:
                return None
            else:
                if a <= target_time and b >= target_time:
                    counter += 1
        return counter
