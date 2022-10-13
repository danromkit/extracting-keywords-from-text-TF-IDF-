from Project.Task_2.extra_steps.correct_start_index.correct_start_index import correct_start_index
from Project.Task_2.extra_steps.end_position.end_position import end_position


def getting_list_beginning_articles(text: str) -> list:
    # Part 1 (Поиск УДК)
    article_position_with_content_start = []
    update_text = end_position("СОДЕРЖАНИЕ", text, article_position_with_content_start)
    # поиск буквы "к" в слове УДК
    count_udk = text.count("УДК", article_position_with_content_start[-1])
    while count_udk != 0:
        update_text = end_position("УДК", update_text, article_position_with_content_start)
        count_udk = update_text.count("УДК", article_position_with_content_start[-1])

    # корректировка индексов начала для всего текста
    article_position_without_content_start = correct_start_index(article_position_with_content_start)
    contents_index = article_position_with_content_start[0]
    article_position_without_content_start.pop(0)

    return article_position_without_content_start
