def study_schedule(permanence_period, target_time):
    try:
        aux = 0

        for item in permanence_period:
            if target_time >= item[0] and target_time <= item[1]:
                aux += 1

        return aux
    except TypeError:
        return None
