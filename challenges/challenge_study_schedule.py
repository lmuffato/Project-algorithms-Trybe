# validação de inteiro
# https://www.delftstack.com/howto/python/python-check-variable-type/#:~:text=variable%20in%20Python.-,Use%20the%20type()%20Function%20to%20Check%20Variable%20Type%20in,return%20the%20variable%20data%20type.


def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for element in permanence_period:
            a = element[0]
            b = element[1]
            if a <= target_time and b >= target_time:
                counter += 1
        return counter
    except TypeError:
        return None
