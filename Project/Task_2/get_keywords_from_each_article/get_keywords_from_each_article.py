from Project.Task_2.extra_steps.correct_start_index.correct_start_index import correct_start_index
from Project.Task_2.extra_steps.end_position.end_position import end_position


def get_list_of_keywords_for_each_article(text: str) -> list:
    keyword_positions = []
    update_text = end_position("Ключевые слова", text, keyword_positions)
    count_keyword = update_text.count("Ключевые слова", keyword_positions[-1])
    while count_keyword != 0:
        update_text = end_position("Ключевые слова", update_text, keyword_positions)
        count_keyword = update_text.count("Ключевые слова", keyword_positions[-1])

    # корректировка индексов начала для всего текста
    keyword_positions = correct_start_index(keyword_positions)

    # Поверка
    print("Длина keyword_positions: ", len(keyword_positions))
    print("Count: ", text.count("Ключевые слова"))

    return keyword_positions
