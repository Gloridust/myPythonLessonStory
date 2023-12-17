# 安装依赖
# pip install requests beautifulsoup4

# 导入所需的库
import requests  # 引入 requests 库，用于向网站发送网络请求
from bs4 import BeautifulSoup  # 引入 BeautifulSoup，用于解析和操作 HTML

# 网络爬虫的目标 URL
url = "https://www.ygeeker.com/"  # 定义变量 url，存储要爬取的网站地址

# 向目标网址发送 GET 请求
response = requests.get(url)  # 使用 requests.get() 方法向指定的 URL 发送 GET 请求，并将响应对象存储在变量 response 中

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')  # 使用 BeautifulSoup 解析 response 对象中的文本内容。这里 'html.parser' 是用于解析 HTML 的解析器

# 查找并打印所有的 div 标签中的文本
paragraphs = soup.find_all('div')  # 使用 BeautifulSoup 的 find_all 方法查找页面上所有的 <div> 标签，并将它们存储在变量 paragraphs 中
for paragraph in paragraphs:  # 遍历 paragraphs 中的每一个元素（每一个 <div> 标签）
    print(paragraph.text)  # 打印出 <div> 标签中的文本内容