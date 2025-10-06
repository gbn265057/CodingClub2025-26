import requests
from bs4 import BeautifulSoup
import time

url = 'https://icanhazdadjoke.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

joke = soup.find('div', class_ = 'card-content')
joke = joke.text

for letter in joke:
    print(letter, end = '', flush=True)
    if (letter != '?' and letter != '.' and letter != '!'):
        time.sleep(0.1)
    else:
        time.sleep(1.5)
