from Project.Task_3.IDF.IDF import IDF
from Project.Task_3.TF.TF import TF


def TF_IDF(texts: list) -> list:
    tf_idf_line_list = []
    for line in texts:
        tf_dict, keys, values = TF(line)
        idf_dict, idf_line, word_in_line = IDF(texts, keys)
        for i in tf_dict:
            tf_idf_word = tf_dict[i] * idf_dict[i]
            tf_dict[i] = tf_idf_word
        tf_dict_list_2 = sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)
        tf_idf_line_list.append(tf_dict_list_2[:20])

    return tf_idf_line_list
