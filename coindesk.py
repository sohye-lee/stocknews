import requests
from bs4 import BeautifulSoup

coindesk = "https://www.coindesk.com/news"
def coindesk_news():
    res = requests.get(coindesk)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_list = soup.find_all("div", {"class": "text-content"})
    news = []
    for n in news_list:
        a = n.find_all("a")[1]
        title = a.find("h4", {"class": "heading"}).text
        link = "https://coindesk.com" + a['href']
        author_box = n.find("span", {"class": "credit"}).find("a")
        author = author_box.text
        writtenAt = n.find("time", {"class": "time"}).text
        news.append({"website": "Coindesk", 'title': title, "link": link, "author": author, "writtenAt": writtenAt})
    return news
