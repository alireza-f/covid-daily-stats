from bs4 import BeautifulSoup
import requests
import json
import lxml.html
import time

daily_stats = list()

def crawl():
    today_stats = dict()
    url = 'https://www.worldometers.info/coronavirus/country/iran/'
    page = requests.get(url).content
    doc = lxml.html.fromstring(page)
    stats = doc.xpath(
        '//div[@class="news_post"]/div[@class="news_body"]/ul[@class="news_ul"]//li[@class="news_li"]/strong/text()'
        )[:2]
    today = doc.xpath('//div[@class="news_date"]/h4/text()')[0]
    today_stats[today] = {'New Cases': stats[0], 'New Deaths': stats[1]}
    daily_stats.append(today_stats)
    print(today, stats)


while True:
    crawl()
    with open('daily-stats.json', 'w') as fp:
        json.dump(daily_stats, fp, ensure_ascii=False)
    time.sleep(5)
    

