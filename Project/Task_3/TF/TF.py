import collections


def TF(text: list) -> list:
    tf_text = collections.Counter(text)
    tf_text_list = []
    for i in tf_text:
        tf_text[i] = tf_text[i] / float(len(text))
        tf_text_list.append(tf_text[i] / float(len(text)))

    return tf_text, tf_text.keys(), tf_text.values()
