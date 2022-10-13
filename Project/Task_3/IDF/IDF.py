import math


def IDF(texts: list, word_in_line: list) -> list:
    idf_line = []
    for word in word_in_line:
        idf_word = math.log10(len(texts) / sum([1.0 for i in texts if word in i]))
        idf_line.append(idf_word)
        idf_dict = dict(zip(word_in_line, idf_line))

    return idf_dict, idf_line, word_in_line
