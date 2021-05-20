import requests
from bs4 import BeautifulSoup

bitcoinist = "https://bitcoinist.com/"
def bitcoinist_news():
    res = requests.get(bitcoinist)
    soup = BeautifulSoup(res.text, 'html.parser')
    news = []
    news_boxes = soup.find_all("div", {"class": "archive-posts"})
    for b in news_boxes:
        news_list = b.find_all("article", {"class": "jeg_post"})
        for n in news_list[2:]:
            h3 = n.find("h3", {"class": "jeg_post_title"})
            a = h3.find("a")
            title = a.text
            link = a['href']
            author_box = n.find("div", {"class": "jeg_meta_author"})
            author_a = author_box.find("a")
            author = author_a.text
            writtenAt = n.find("div", {"class": "jeg_meta_date"}).find("a").text[1:]
            news.append({"website": "Bitcoinist", 'title': title, "link": link, "author": author, "writtenAt": writtenAt})
    return news
