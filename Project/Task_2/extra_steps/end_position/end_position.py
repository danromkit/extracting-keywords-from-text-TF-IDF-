# извлечение позиции конца всех ключевых слов
def end_position(word: str, text: str, end: list) -> str:
    word_length = len(word)
    word_index = text.find(word) + word_length  # ищу индекс первой буквы интересущего меня слова
    new_text = text[word_index:]
    end.append(word_index)  # добавляет индекс пробела идущего за интересующем нас словом

    return new_text
