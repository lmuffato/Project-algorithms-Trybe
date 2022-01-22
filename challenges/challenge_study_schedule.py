def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for pp in permanence_period:
            if target_time >= pp[0] and target_time <= pp[1]:
                count += 1
        return count
    except Exception:
        return None


""" def study_schedule(permanence_period, target_time):
    count = 0
    for pp in permanence_period:
        if target_time is None or type(pp[0])
        is not int or type(pp[1]) is not int:
            return None
        if target_time in range(pp[0], pp[1]+1):
            count += 1
    return count """


""" permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
teste = study_schedule(permanence_period, 5)
print(teste) """
