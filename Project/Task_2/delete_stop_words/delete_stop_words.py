from nltk.corpus import stopwords

stop_words = list(set(stopwords.words("russian")))


# Удаление стоп слов
def delete_stop_words(text: list) -> list:
    tokens_without_sw = [word for word in text if not word in stopwords.words()]

    return tokens_without_sw
