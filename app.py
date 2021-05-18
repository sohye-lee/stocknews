import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

from coindesk import coindesk_news
from cryptoslate import cryptoslate_news

app = Flask('StockNews')



@app.route('/')
def home():
    cd_news = coindesk_news()
    cs_news = cryptoslate_news()
    all_news = cd_news + cs_news
    num_news = len(cd_news) + len(cs_news)
    return render_template('index.html', all_news=all_news, num_news=num_news)

# cryptoslate_news()

app.run(host="127.0.0.1", port=8080)