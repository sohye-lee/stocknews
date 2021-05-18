import requests
from bs4 import BeautifulSoup

cryptoslate = "https://www.cryptoslate.com/news/"

def data_per_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_list = soup.find_all("div", {"class": "list-post"})
    news = []
    for n in news_list:
        a = n.find("a")
        link = a['href']
        title = n.find("div", {"class": "title"}).find('h2').text
        texts = n.find("span", {"class": "post-meta"}).text[:-3].split(" · ")
        author = texts[0]
        writtenAt = texts[1]
        news.append({"website": "Cryptoslate", 'title': title, "link": link, "author": author, "writtenAt": writtenAt})
    return news

def cryptoslate_news():
    news = []
    for i in range(1,4):
        url = f"{cryptoslate}page/{i}"
        li_per_page = data_per_page(url)
        news += li_per_page
    return news