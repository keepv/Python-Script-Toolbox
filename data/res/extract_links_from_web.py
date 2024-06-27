import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_html_content(base_url, relative_path):
    """通过HTTP请求获取HTML内容"""
    full_url = urljoin(base_url, relative_path)  # 将基URL与相对路径组合成完整URL
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve content from {full_url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching {full_url}: {e}")
        return None

def extract_links_from_html(base_url, html_content):
    """从HTML内容中提取所有链接，并将其转换为绝对URL（如果它们是相对的）"""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    absolute_links = []
    for link in links:
        href = link.get('href')
        if href is not None:
            absolute_link = urljoin(base_url, href)  # 确保链接是绝对的
            absolute_links.append((absolute_link, is_absolute_url(href)))
    return absolute_links

def is_absolute_url(url):
    """判断给定的URL是否为绝对路径"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# 定义基URL和相对路径列表（模拟之前找到的文件路径）
base_url = "http://example.com/"  # 假设这是你的基础URL
relative_paths = [
    # 这里应该填入相对路径列表，这些路径相对于base_url
    # 例如: "somepage.html", "folder/anotherpage.html"
]

# 提取和打印链接URL及路径类型
for path in relative_paths:
    full_url = urljoin(base_url, path)
    print(f"\nExtracting links from {full_url}:")
    html_content = fetch_html_content(base_url, path)
    if html_content is not None:
        link_data = extract_links_from_html(base_url, html_content)
        for link_url, was_relative in link_data:
            path_type = "Absolute" if was_relative else "Originally Absolute"
            print(f"{link_url} ({path_type})")