import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')

movies = []
titles = soup.find_all(name='h3', class_='title')

for i in titles:
    with open('movies.txt', 'a',encoding="utf-8" ) as file:
        file.write(i.getText()+"\n")
