def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    on_line = 0
    for horario in permanence_period:
        if not horario[0] or not horario[1]:
            return None
        if horario[0] <= target_time <= horario[1]:
            on_line += 1

    return on_line
