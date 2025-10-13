# import requests as req
# import bs4
from newsapi import NewsApiClient

# r = req.get("https://newsapi.org/v2/everything?q=tesla&from=2024-07-11&sortBy=publishedAt&apiKey=22632c60ca9b42b588fea749357709f0")
# soup = bs4.BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())


# Init
newsapi = NewsApiClient(api_key='22632c60ca9b42b588fea749357709f0')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',sources='bbc-news,the-verge',category='business',language='en',country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',sources='bbc-news,the-verge',domains='bbc.co.uk,techcrunch.com',from_param='2017-12-01',to='2017-12-12',language='en',sort_by='relevancy',page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()