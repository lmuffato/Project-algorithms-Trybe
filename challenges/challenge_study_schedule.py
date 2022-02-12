def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    usuarios_online = 0
    # para cada tempo de entrada e tempo de saída em permanence_period
    for tempo_inicio, tempo_saida in permanence_period:
        # Se não tiver tempo de entrada ou saída
        if not tempo_inicio or not tempo_saida:
            return None
        if tempo_inicio <= target_time <= tempo_saida:
            usuarios_online += 1
    return usuarios_online


# Teste Manual
# permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_periods, 1))
