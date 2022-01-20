def study_schedule(permanence_period, target_time):
    count = 0
    for p in permanence_period:
        if type(p[0]) != int or type(p[1]) != int or type(target_time) != int:
            return None
        index = p[0]
        while index <= p[1]:
            if index == target_time:
                count += 1
            index += 1
    return count
