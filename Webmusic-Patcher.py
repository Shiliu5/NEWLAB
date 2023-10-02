import requests
from bs4 import BeautifulSoup
import os

# 定义抓取网页的URL
url = "http://example.com/mp3page"  # 替换为你要抓取的网页URL

# 发送HTTP请求并获取页面内容
response = requests.get(url)

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(response.content, "html.parser")

# 找到页面中的所有链接
links = soup.find_all("a")

# 定义一个目录来保存抓取到的MP3文件
download_directory = "mp3_files"
os.makedirs(download_directory, exist_ok=True)

# 遍历链接并下载MP3文件
for link in links:
    href = link.get("href")
    if href and href.endswith(".mp3"):
        mp3_url = href
        mp3_filename = os.path.join(download_directory, os.path.basename(mp3_url))
        try:
            mp3_response = requests.get(mp3_url)
            with open(mp3_filename, "wb") as mp3_file:
                mp3_file.write(mp3_response.content)
            print(f"已下载：{mp3_filename}")
        except Exception as e:
            print(f"下载失败：{mp3_url}，错误：{str(e)}")
