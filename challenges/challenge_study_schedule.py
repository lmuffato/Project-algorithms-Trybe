def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None
    else:
        logged_students = 0
        for session in permanence_period:
            # all() Retorna `True` se todos os elementos do iterável forem
            # verdadeiros (ou se o iterável for vazio). Ou seja, a função
            # recebe como parâmetro um objeto iterável (uma lista ou uma
            # tupla, por exemplo) e verifica se todos os elementos desse
            # iterável possuem o valor True
            if not all(session):
                return None
            if session[0] <= target_time <= session[1]:
                logged_students += 1
    return logged_students
