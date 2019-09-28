import requests
import re
from bs4 import BeautifulSoup as bs


def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic
    return link


def get_topic_page(topic):
    link = get_link(topic)
    html_content = requests.get(link).text
    return html_content


def get_link_on_sites(topic):
    # list_of_wiki = re.findall('href="(/wiki/[\d\w%]+)[^ ]+', get_topic_page(topic))
    wiki_list = bs(get_topic_page(topic), "html.parser")
    list_wiki = wiki_list.find_all("a")
    list_wiki_sites = []
    for n in list_wiki:
        find_href = n.get("href", "")
        if "/wiki/" in find_href:
            if ".jpg" in find_href:
                continue
            elif ".svg" in find_href:
                continue
            else:
                numb_for_start = find_href.find("/wiki/")
                list_wiki_sites.append(find_href[numb_for_start + 6:])
    link_list = []
    for link in list_wiki_sites:
        link_list.append(link)
    # print(link_list)
    return link_list
