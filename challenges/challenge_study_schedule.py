def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    # permanence_period -[(hora entrada, hora saida)]
    quant_students = 0

    if target_time is None:
        return None

    for periods in permanence_period:
        if int(all(periods)):
            if periods[0] <= target_time and target_time <= periods[1]:
                quant_students += 1
        else:
            return None
    return quant_students
