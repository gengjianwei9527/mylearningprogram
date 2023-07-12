import requests
from bs4 import BeautifulSoup
import urllib
import os

# 发送请求，获取HTML
url = 'https://www.zhihu.com/tardis/bd/art/453187893?source_id=1001'
response = requests.get(url)
html = response.text

# 解析HTML，获取所有图片链接
soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')
img_urls = [img['src'] for img in img_tags]

# 创建文件夹并下载图片
folder_name = 'images'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for url in img_urls:
    filename = os.path.join(folder_name, url.split('/')[-1])
    urllib.request.urlretrieve(url, filename)
    print(f'Saved {filename}')