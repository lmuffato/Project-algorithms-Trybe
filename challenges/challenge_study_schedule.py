def validate_permanence_period(element):

    if type(element[0]) is not int:
        return False
    if type(element[1]) is not int:
        return False

    return True


def study_schedule(permanence_period, target_time):

    if not target_time:
        return None

    counter = 0

    for element in permanence_period:
        if not validate_permanence_period(element):
            return None
        if element[0] <= target_time <= element[1]:
            counter += 1

    return counter
