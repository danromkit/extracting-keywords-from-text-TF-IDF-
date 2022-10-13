def article_text_extraction(start: list, text: str) -> list:
    articles_text = []
    a = len(start)
    for i in range(len(start)):
        if i != len(start) - 1:
            new_text = text[start[i]:start[i + 1]]
            word = "СПИСОК ЛИТЕРАТУРЫ"
            word_index = new_text.find(word)  # ищу индекс первой буквы интересущего меня слова
            new_text = new_text[:word_index]
            articles_text.append(new_text)
        else:
            new_text = text[start[i]:]
            word = "СПИСОК ЛИТЕРАТУРЫ"
            word_index = new_text.find(word)  # ищу индекс первой буквы интересущего меня слова
            new_text = new_text[:word_index]
            articles_text.append(new_text)

    return articles_text
