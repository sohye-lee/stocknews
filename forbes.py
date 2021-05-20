import requests
from bs4 import BeautifulSoup

forbes = "https://www.forbes.com/crypto-blockchain"
def forbes_news():
    res = requests.get(forbes)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_container = soup.find("div", {"class": "chansec-stream__items"})
    news_list = news_container.find_all("article", {"class": "stream-item"})
    news = []
    for n in news_list:
        a = n.find("a", {"class": "stream-item__title"})
        title = a.text
        link =  a['href']
        author = n.find("a", {"class": "byline__author-name"}).text
        writtenAt = n.find("div", {"class": "stream-item__date"}).text
        news.append({"website": "Forbes", 'title': title, "link": link, "author": author, "writtenAt": writtenAt})
    return news