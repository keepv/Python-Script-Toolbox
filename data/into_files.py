如果您想搜索没有特定后缀的文件，并且筛选文件名中包含特定关键词的文件，可以修改代码以适应这种需求。以下是相应的示例代码：

### 示例代码

假设您想在当前目录及其子目录中搜索文件名包含特定关键词的文件，然后对这些文件进行处理。

```python
import os

def find_files_with_keyword(directory, keyword):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower() and '.' not in file:
                matches.append(os.path.join(root, file))
    return matches

# 定义要搜索的目录和关键词
directory_to_search = '.'
keyword_to_search = 'sample'  # 你可以根据需要修改关键词

# 搜索文件
matching_files = find_files_with_keyword(directory_to_search, keyword_to_search)

# 打印找到的文件
print("Found files:")
for file in matching_files:
    print(file)
```

### 说明：

1. **导入模块**：导入`os`模块用于文件系统操作。
2. **定义`find_files_with_keyword`函数**：该函数遍历指定目录及其子目录，搜索文件名中包含特定关键词且没有文件后缀的文件，并返回匹配的文件路径列表。
    - `if keyword.lower() in file.lower() and '.' not in file:` 判断文件名是否包含关键词且不包含`.`字符（即没有文件后缀）。
3. **设置要搜索的目录和关键词**：定义要搜索的目录和关键词，目录默认为当前目录`'.'`，关键词可以根据需要修改。
4. **搜索文件**：调用`find_files_with_keyword`函数，获取匹配的文件列表。
5. **打印找到的文件**：遍历并打印匹配的文件路径。

通过这种方式，您可以自动搜索所有文件，选择文件名中包含特定关键词且没有后缀的文件。如果有任何问题或需要进一步的帮助，请告诉我。