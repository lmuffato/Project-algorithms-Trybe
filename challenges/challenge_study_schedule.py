def study_schedule(permanence_period, target_time):
    students = []
    for start_time, finish_time in permanence_period:
        # Fontes:
        # https://www.w3schools.com/python/ref_func_isinstance.asp
        # https://pynative.com/python-isinstance-explained-with-examples/
        # https://www.youtube.com/watch?v=Yoi8gh9x5PU
        # Checando se as entradas de permanence period são válidas
        if (not isinstance(start_time, int)
                or not isinstance(finish_time, int)
                or target_time is None):
            return None
        if (start_time <= target_time <= finish_time):
            students.append((start_time, finish_time))
    return len(students)
