def study_schedule(permanence_period, target_time):
    conunter = 0

    try:
        for index in permanence_period:
            if target_time >= index[0] and target_time <= index[1]:
                conunter += 1
    except TypeError:
        return None
    return conunter


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
