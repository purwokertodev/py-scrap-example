import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrap_webpage():
    web_page = 'https://news.ycombinator.com/'

    page = requests.get(web_page, timeout=5)

    soup = BeautifulSoup(page.content, "html.parser")

    news_row = soup.find_all('tr', {'class': ['athing']})
    news = []

    for story in news_row:
        tds = story.find_all('td', {'class': ['title']})
        news.append([tds[1].find('a', {'class': ['storylink']}).text, tds[1].find('a')['href']])
    
    df = pd.DataFrame.from_records(news, columns=['title','link'])

    return df.to_csv(index=False)

def save_file(data):
    with open('data.csv', 'w') as csv_file:
        csv_file.write(data)


def main():
    data = scrap_webpage()
    save_file(data)


if __name__ == '__main__':
    main()