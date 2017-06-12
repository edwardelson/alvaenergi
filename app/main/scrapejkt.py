"""
Web Scraping

pull data from http://smartcity.jakarta.go.id/blog
pull data from http://smartcity.jakarta.go.id/events
"""

import requests
from bs4 import BeautifulSoup

# update from smartcity blog
def updateJKTBlog():
    blog = requests.get("http://smartcity.jakarta.go.id/blog")
    soup = BeautifulSoup(blog.content, 'html.parser')

    # extract newest blog entries from smartcity website
    news = soup.find(id="news")
    # list of newest [blog title, URL] -> read html source from smartcity website
    newsList = [{'title':data.get_text(), 'url':data.find('a')['href']} \
        for data in news.select(".news-pad .news-vh .spc")]

    return newsList

# update from smartcity events
def updateJKTEvents():
    blog = requests.get("http://smartcity.jakarta.go.id/events")
    soup = BeautifulSoup(blog.content, 'html.parser')

    # extract newest blog entries from smartcity website
    events = soup.find(id="news")
    # list of newest [blog title, URL] -> read html source from smartcity website
    eventsList = [{'title':data.get_text(), 'url':data.find('a')['href']} \
        for data in events.select(".news-pad .news-vh .spc")]

    return eventsList
