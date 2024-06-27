import os
from bs4 import BeautifulSoup

def find_files_with_keyword(directory, keyword):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower() and file.endswith('.html'):
                matches.append(os.path.join(root, file))
    return matches

def extract_links_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    link_urls = [link['href'] for link in links if 'href' in link.attrs]
    return link_urls

# 定义要搜索的目录和关键词
directory_to_search = '.'
keyword_to_search = 'sample'  # 你可以根据需要修改关键词

# 搜索文件
matching_files = find_files_with_keyword(directory_to_search, keyword_to_search)

# 打印找到的文件
print("Found files:")
for file in matching_files:
    print(file)

# 提取和打印链接URL
for file in matching_files:
    print(f"\nExtracting links from {file}:")
    link_urls = extract_links_from_html(file)
    for url in link_urls:
        print(url)