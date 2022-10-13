import re


def clear_text(text: list) -> list:
    clear_list_of_articles = []
    for i in text:
        clear_text = re.sub(r'[^\w\s]+|[\d]+', r'', i).strip()
        clear_text = re.sub(r'[.,"\'-?:!;]', '', clear_text)
        clear_list_of_articles.append(clear_text)

    return clear_list_of_articles
