# Упражнение продолжает практическую работу из последнего видеоурока. Для усовершенствования приложения разберитесь,
# как можно реализовать получение common words с соседних страниц — тех, на которые есть ссылки. Возможен следующий
# алгоритм решения задачи: 1. Получить ссылки на соседние страницы. Для этого можно воспользоваться библиотекой
# BeautifulSoup. Не забудьте отобрать только правильные ссылки, которые указывают на другие страницы Википедии. (Вы
# можете распознать их по тексту \wiki). 2. Спарсить отдельно соседние страницы. Для этого вам необходимо перебрать в
# цикле все полученные ссылки. 3. Сложить все в один список.

import re
from Lesson_4_wiki_request import get_topic_page
from Lesson_4_wiki_request import get_link_on_sites


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']{3,}", html_content)
    return words


def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[100:110]:
        print(w[0])


def get_all_topic_words(topic):
    all_topic_pages = get_link_on_sites(topic)
    html_words = []
    for link in all_topic_pages[:20]:
        # здесь можно посмотреть больше ссылок, если убрать срез, но чем больше ссылок тем дольше обрабатывает.
        html_content = get_topic_words(link)
        html_words = html_words + html_content
    return html_words


def get_all_common_words(topic):
    topic_words = get_all_topic_words(topic)
    all_rates = {}
    for word in topic_words:
        if word in all_rates:
            all_rates[word] += 1
        else:
            all_rates[word] = 1
    rate_all_words = list(all_rates.items())
    rate_all_words.sort(key=lambda x: -x[1])
    return rate_all_words


def visualize_common_words_in_all_sites(topic):
    all_words_in_all_sites = get_all_common_words(topic)
    # print(all_words_in_all_sites)
    # print(len(all_words_in_all_sites))
    print('Слова из ссылок: ')
    for w in all_words_in_all_sites[180:]:
        # здесь можно выбрать срез слов или вывести все слова
        print(w[0])


topic = input("Topic: ")
visualize_common_words(topic)
visualize_common_words_in_all_sites(topic)