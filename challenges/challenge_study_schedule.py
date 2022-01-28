def validate_permanence_period(permanence_period):

    for element in permanence_period:
        if type(element[0]) != int:
            return None
        if type(element[1]) != int:
            return None

    return True


def validate_target_time(target_time):
    if not target_time:
        return None

    return True


def study_schedule(permanence_period, target_time):

    if (
        validate_permanence_period(permanence_period)
        and validate_target_time(target_time)
    ):
        counter = 0

        for element in permanence_period:
            if element[0] == target_time:
                counter += 1
            if element[1] == target_time:
                counter += 1

        return counter
