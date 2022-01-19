def validate_tuples(tpList):
    return type(tpList[0]) == int and type(tpList[1]) == int


def study_schedule(permanence_period, target_time):
    numberStudents = 0
    if target_time is None:
        return None
    for tp in permanence_period:
        if not all(tp):
            return None
        if tp[0] <= target_time and tp[1] >= target_time:
            numberStudents += 1
    return numberStudents
