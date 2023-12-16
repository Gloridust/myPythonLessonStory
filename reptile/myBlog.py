import requests
from bs4 import BeautifulSoup
import os

def get_article_links(main_page_url):
    # Fetch the main page and extract article links
    # response = requests.get(main_page_url)    修改请求代码，添加一个参数来禁用 SSL 验证
    response = requests.get(main_page_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all(...)  # Modify this to match your blog's structure
    return [link['href'] for link in links]

def download_article_content_and_images(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract content
    content = soup.find(p)  # Modify this based on your article's HTML structure
    # Save content to a text file

    # Extract and download images
    images = soup.find_all('img')
    for img in images:
        img_url = img['src']
        # Code to download and save the image

def main():
    main_page_url = 'https://gloridust.xyz'
    article_links = get_article_links(main_page_url)

    for url in article_links:
        download_article_content_and_images(url)

if __name__ == '__main__':
    main()
