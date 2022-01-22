def study_schedule(permanence_period, target_time):
    # """ Faça o código aqui. """
    if target_time == "":
        return None
    else:
        for start, end in permanence_period:
            if start == "" or end == "":
                return None
