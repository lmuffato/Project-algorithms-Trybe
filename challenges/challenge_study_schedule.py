def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    # permanence_period -[(hora entrada, hora saida)]
    # print(permanence_period)
    # https://stackoverflow.com/questions/58656740/python-check-if-tuple-contain-only-integers-with-while
    # https://www.w3schools.com/python/ref_func_isinstance.asp
    # quant_students = 0

    if target_time is None:
        return None

    for period in permanence_period:
        if isinstance(period, int):
            return None
