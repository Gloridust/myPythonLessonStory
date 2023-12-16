import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_article_links(blog_url):
    """获取博客文章的链接列表"""
    response = requests.get(blog_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 假设每篇文章的链接都在<a>标签内，您需要根据实际情况调整选择器
    links = soup.find_all('a', class_='article-link')  # 修改class为您博客的相应class
    return [urljoin(blog_url, link['href']) for link in links]

def save_article_content(url, folder_path):
    """保存文章内容和图片"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假设文章内容在一个特定的<div>标签内
    article_content = soup.find('div', class_='article-content')  # 修改class为您博客的相应class

    # 保存文章文本
    with open(os.path.join(folder_path, 'article.txt'), 'w', encoding='utf-8') as file:
        file.write(article_content.text)

    # 保存文章内的图片
    images = article_content.find_all('img')
    for i, img in enumerate(images):
        img_url = urljoin(url, img['src'])
        img_data = requests.get(img_url).content
        with open(os.path.join(folder_path, f'image_{i}.jpg'), 'wb') as file:
            file.write(img_data)

# 主函数
def main():
    blog_url = 'https://gloridust.xyz'  # 您博客的URL
    article_links = get_article_links(blog_url)

    for url in article_links:
        folder_name = url.split('/')[-1]  # 假设文章的标题是URL的最后一部分
        folder_path = os.path.join('articles', folder_name)
        os.makedirs(folder_path, exist_ok=True)
        save_article_content(url, folder_path)

if __name__ == "__main__":
    main()
