# корректировка индексов начала для всего текста
def correct_start_index(position_start: list) -> list:
    for i in range(1, len(position_start)):
        position_start[i] += position_start[i - 1]

    return position_start
