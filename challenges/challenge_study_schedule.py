def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    sum = 0
    length = len(permanence_period)

    for index in range(length):
        period_min, period_max = permanence_period[index]

        if type(period_min) != int or type(period_max) != int:
            return None

        if period_min <= target_time <= period_max:
            sum += 1

    return None if sum == 0 else sum

# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
