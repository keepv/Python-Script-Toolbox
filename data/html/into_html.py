import os
from bs4 import BeautifulSoup

def find_files_with_keyword(directory, keyword):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower() and file.endswith('.html'):
                matches.append(os.path.join(root, file))
    return matches

def extract_image_urls_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    image_urls = [img['src'] for img in images]
    return image_urls

# 定义要搜索的目录和关键词
directory_to_search = '.'
keyword_to_search = 'sample'  # 你可以根据需要修改关键词

# 搜索文件
matching_files = find_files_with_keyword(directory_to_search, keyword_to_search)

# 打印找到的文件
print("Found files:")
for file in matching_files:
    print(file)

# 提取和打印图片URL
for file in matching_files:
    print(f"\nExtracting images from {file}:")
    image_urls = extract_image_urls_from_html(file)
    for url in image_urls:
        print(url)