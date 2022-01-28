from tokenize import Number


def study_schedule(permanence_period, target_time):

    if not target_time:
        return None

    for element in permanence_period:
        if type(element[0]) != int:
            return None
        if type(element[1]) != int:
            return None

    counter = 0

    for element in permanence_period:
        if element[0] == target_time:
            counter += 1
        if element[1] == target_time:
            counter += 1

    return counter
