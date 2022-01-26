def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for entry, exit_time in permanence_period:
            if entry <= target_time <= exit_time:
                students += 1
        return students
    except TypeError:
        return None

# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/reference/compound_stmts.html
# Nos arrays temos 6 estudantes
# estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
