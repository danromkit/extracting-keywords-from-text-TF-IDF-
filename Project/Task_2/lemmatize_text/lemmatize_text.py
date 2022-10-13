import pymorphy2

from Project.Task_2.delete_stop_words.delete_stop_words import delete_stop_words
from nltk.tokenize import sent_tokenize, word_tokenize


def lemmatize_text(texts: list) -> list:
    morph = pymorphy2.MorphAnalyzer()
    for text in range(len(texts)):
        texts[text] = texts[text].lower()
        texts[text] = word_tokenize(texts[text])
        # Удаление стоп слов
        texts[text] = delete_stop_words(texts[text])
        # Лемматизация
        for i in range(len(texts[text])):
            texts[text][i] = morph.parse(texts[text][i])[0].normal_form
            print(1)

    return texts
