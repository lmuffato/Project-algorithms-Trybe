def study_schedule(permanence_period, target_time):
    try:
        num_of_students = 0
        for entry_time, exite_time in permanence_period:
            if entry_time <= target_time <= exite_time:
                num_of_students += 1
        return num_of_students

    except TypeError:
        return None


# permanence_period = [(2, "2"), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, 5))
