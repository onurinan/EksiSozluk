import requests
from bs4 import BeautifulSoup as bs

url = "https://eksisozluk.com/"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers = headers)

soup = bs(r.content, "lxml")

linkler = soup.find("ul", attrs = {"class" : "topic-list partial"}).text

print(linkler)
