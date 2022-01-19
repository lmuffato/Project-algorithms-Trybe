def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for period in permanence_period:
        # https://stackoverflow.com/questions/31154372/what-is-the-best-way-to-check-if-a-tuple-has-any-empty-none-values-in-python
        if not all(period):
            return None
        if period[0] <= target_time <= period[1]:
            counter += 1
    return counter
