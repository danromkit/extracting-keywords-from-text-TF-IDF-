from Project.Task_1.data_loading.data_loading import data_loading
from Project.Task_2.article_text_extraction.article_text_extraction import article_text_extraction
from Project.Task_2.clear_text.clear_text import clear_text
from Project.Task_2.getting_list_beginning_articles.getting_list_beginning_articles import \
    getting_list_beginning_articles
from Project.Task_2.lemmatize_text.lemmatize_text import lemmatize_text
from Project.Task_3.TF_IDF.TF_IDF import TF_IDF
from config import pdf

# Task 1
text = data_loading(pdf)

# Task 2
# Извлечение списка статей
article_start_list = getting_list_beginning_articles(text)
list_of_articles = article_text_extraction(article_start_list, text)

# Очистка текста
clear_list_of_articles = clear_text(list_of_articles)

# Лемматизация текста
tokenize_texts = lemmatize_text(clear_list_of_articles)

# TF_IDF
tf_idf = TF_IDF(tokenize_texts)
print(tf_idf)
