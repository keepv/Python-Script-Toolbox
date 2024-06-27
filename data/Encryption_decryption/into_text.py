import os

# 设置当前工作目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 构造完整的文件路径
    file_path = os.path.join(current_directory, filename)
    txt_file_path = file_path + '.txt'
    
    # 检查文件名是否没有后缀
    if '.' not in filename:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 如果对应的.txt文件不存在，则创建它
        if not os.path.exists(txt_file_path):
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(content)
            print(f"创建新文件: {txt_file_path}")
        else:
            # 如果.txt文件已存在，则替换其内容
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(content)
            

print("所有文件处理完成")
