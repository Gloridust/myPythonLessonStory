# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.ygeeker.com/"  # 用您想要爬取的网址替换
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

paragraphs = soup.find_all('div')
for paragraph in paragraphs:
    print(paragraph.text)