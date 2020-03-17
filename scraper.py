import requests
from bs4 import BeautifulSoup

URL = 'https://www.nytimes.com/2020/03/13/world/coronavirus-news.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('ul', class_='css-1gfen40 ez3869y0')
headlines = []

for line in results:
    line = str(line) + "\n"
    headlines.append(line)

for result in results:
    print("\n" + result.text)

    